from language.python import ast
from analysis.dataflowIR import graph
from analysis.dataflowIR import annotations

from translator.glsl import intrinsics

def makeCorrelatedAnnotation(dioa, data):
	return annotations.CorrelatedAnnotation(dioa.set.flatten(data), data)

def getName(subtree, root):
	name = 'bogus'

	if subtree.name:
		name = subtree.name
	elif isinstance(root, graph.LocalNode):
		for lcl in root.names:
			if lcl.name:
				name = lcl.name
				break
	return name

def createLocalNode(hyperblock, name, values):
	lcl  = ast.Local(name)
	node = graph.LocalNode(hyperblock, (lcl,))
	annotation = annotations.DataflowSlotAnnotation(values, True)
	node.annotation = annotation

	return node

def addOutput(g, subtree, original):
	if hasattr(original, 'annotation'):
		values = original.annotation.values
	else:
		values = original
	
	node = createLocalNode(g.hyperblock, getName(subtree, original), values)

	g.addLocalModify(node.names[0], node)

	return node

def allocateObj(dioa, dataflow, subtree, slot, obj):
	hyperblock = dataflow.entry.hyperblock
	predicate  = dataflow.entryPredicate
	objs       = slot.annotation.values.flat

	# Allocate
	assert len(objs) == 1

	obj      = tuple(objs)[0]
	cls      = ast.Existing(obj.xtype.obj.type)
	allocate = ast.Allocate(cls)
	g = graph.GenericOp(hyperblock, allocate)
	
	g.setPredicate(predicate)
	g.addLocalRead(cls, dataflow.getExisting(cls, obj))

	# Build op annotation
	read         = makeCorrelatedAnnotation(dioa, dioa.set.empty)
	modify       = makeCorrelatedAnnotation(dioa, dioa.set.empty)
	allocate     = makeCorrelatedAnnotation(dioa, dioa.set.leaf((obj,)))
	mask         = dioa.bool.true # HACK
	annotation   = annotations.DataflowOpAnnotation(read, modify, allocate, mask)
	g.annotation = annotation
	
	return addOutput(g, subtree, slot)

def transformInputSubtree(compiler, dioa, dataflow, subtree, root):
	hyperblock = dataflow.entry.hyperblock
	predicate  = dataflow.entryPredicate
	objs = root.annotation.values.flat # HACK - what about correlation?

	assert len(objs) > 0
	obj = tuple(objs)[0]

	# HACK temporarily ignore correlated objects.
	if len(objs) > 1:
		exprNode = createLocalNode(hyperblock, getName(subtree, root), root.annotation.values)
		name = exprNode.names[0]
		dataflow.entry.addEntry(name, exprNode)
		subtree.impl = name
	else:	
		assert len(objs) == 1
		if intrinsics.isIntrinsicObject(obj):
			exprNode = createLocalNode(hyperblock, getName(subtree, root), root.annotation.values)
			name = exprNode.names[0]
			dataflow.entry.addEntry(name, exprNode)
			subtree.impl = name
			
			# Prevent the fields of this object from being transformed
			return exprNode
		else:
			exprNode = allocateObj(dioa, dataflow, subtree, root, obj)

	lut = dataflow.entry.modifies

	for field, child in subtree.fields.iteritems():
		# Field the field nodes for the field name
		fieldNodes = [lut[o.slots[field]] for o in objs if field in o.slots]
		
		fieldNode = fieldNodes[0] # HACK
		
		# HACK ignore correlated fields
		#if fieldNode.annotation.values.correlated.tree(): continue
		
		valueNode = transformInputSubtree(compiler, dioa, dataflow, child, fieldNode)
		name = ast.Existing(field.name)
		op = ast.Store(exprNode.names[0], field.type, name, valueNode.names[0])

		g = graph.GenericOp(hyperblock, op) 

		g.setPredicate(predicate)
		g.addLocalRead(exprNode.names[0], exprNode)
		g.addLocalRead(name, dataflow.getExisting(name))
		g.addLocalRead(valueNode.names[0], valueNode)


		for oldField in fieldNodes:
			newField = oldField.duplicate()
			newField.annotation = oldField.annotation
		
			g.addModify(newField.name, newField)
			
			oldField.canonical().redirect(newField)
		
		modifies = dioa.set.leaf(fieldNodes)
		
		read     = makeCorrelatedAnnotation(dioa, dioa.set.empty)
		modify   = makeCorrelatedAnnotation(dioa, modifies)
		allocate = makeCorrelatedAnnotation(dioa, dioa.set.empty)
		mask     = dioa.bool.true # HACK

		annotation = annotations.DataflowOpAnnotation(read, modify, allocate, mask)
		g.annotation = annotation

	return exprNode

def transformInput(compiler, dioa, dataflow, contextIn, root):
	exprNode = transformInputSubtree(compiler, dioa, dataflow, contextIn, root)

	# We create a new local, so replace it.
	if root.isLocal(): root.canonical().redirect(exprNode)


def transformOutputSubtree(compiler, dioa, dataflow, subtree, root):
	hyperblock = dataflow.exit.hyperblock
	predicate = dataflow.exit.predicate
	
	if isinstance(root, graph.LocalNode):
		expr = root.names[0]
	else:
		assert isinstance(root, graph.ExistingNode)
		expr = root.name

	for field, child in subtree.fields.iteritems():
		
		if intrinsics.isIntrinsicField(field): continue
		
		name = ast.Existing(field.name)
		nameref = field.name # HACK incorrect
		op   = ast.Load(expr, field.type, name)
				
		g = graph.GenericOp(hyperblock, op) 

		g.setPredicate(predicate)
		g.addLocalRead(expr, root)
		g.addLocalRead(name, dataflow.getExisting(name, nameref))
		
		reads = dioa.set.empty
		values = dioa.set.empty
		
		for obj, mask in subtree.objMasks.iteritems():
			slot = obj.knownField(field)
			node = dataflow.exit.reads[slot]
		
			g.addRead(slot, node)
			
			reads = dioa.set.union(reads, dioa.set.ite(mask, dioa.set.leaf((node,)), dioa.set.empty)) 
			
			fieldValues = node.annotation.values.correlated
			fieldValues = dioa.set.simplify(mask, fieldValues, dioa.set.empty)
			values = dioa.set.union(values, fieldValues) 
		
		read     = makeCorrelatedAnnotation(dioa, reads)
		modify   = makeCorrelatedAnnotation(dioa, dioa.set.empty)
		allocate = makeCorrelatedAnnotation(dioa, dioa.set.empty)
		mask     = dioa.bool.true # HACK

		annotation = annotations.DataflowOpAnnotation(read, modify, allocate, mask)
		g.annotation = annotation
		
		outputNode = addOutput(g, child,  makeCorrelatedAnnotation(dioa, values))


		# Expose the local at the output.
		name = outputNode.names[0]
		dataflow.exit.addExit(name, outputNode)
		child.impl = name
				
		transformOutputSubtree(compiler, dioa, dataflow, child, outputNode)

def transformOutput(compiler, dioa, dataflow, contextOut, root):
	transformOutputSubtree(compiler, dioa, dataflow, contextOut, root)

def killNonintrinsicIO(compiler, dataflow):
	def callback(name, slot):
		if slot.isField():
			# Kill non-intrinsic fields.
			return intrinsics.isIntrinsicSlot(slot.name)
		elif slot.isLocal():
			# Kill locals that do not contain intrinsic types.
			intrinsicObj = any([intrinsics.isIntrinsicObject(obj) for obj in slot.annotation.values.flat])
			return intrinsicObj

	node = dataflow.exit.filterUses(callback)


# Used for culling the output of the fragment shader.
# Only the built-in outputs of the fragment shader are actually used.
def killUnusedOutputs(context):
	def callback(name, slot):
		if isinstance(name, ast.Local):
			if name not in context.trees.outputLUT:
				return False
			tree = context.trees.outputLUT[name]
			return tree.builtin or tree.link
		else:
			return True

	node = context.dataflow.exit	
	node.filterUses(callback)
	