from .. import intrinsics


class IOTreeObj(object):
	def __init__(self, path, treetype, parent=None):
		self.parent   = parent
		self.path     = path
		self.treetype = treetype
		self.objMasks = {}
		self.fields   = {}

		self.builtin  = False
		self.name     = None
		self.impl     = None

		self.link     = None

	def getField(self, field):
		if not field in self.fields:
			slot = IOTreeObj(self.path + (field,), self.treetype, self)
			self.fields[field] = slot
		else:
			slot = self.fields[field]
		return slot

	def match(self, matcher):
		if isinstance(matcher, dict):
			for field, child in self.fields.iteritems():
				key = field.type, field.name
				
				if key in matcher:
					child.match(matcher[key])
		else:
			self.name = matcher
			self.builtin = True

	def buildImplementationLUT(self, lut):
		if self.impl:
			assert self.impl not in lut, self.impl
			lut[self.impl] = self
			
		for child in self.fields.itervalues():
			child.buildImplementationLUT(lut)
	
	def makeLinks(self, other, uid):
		print "LINK", self.path, other.path
		
		self.link  = other
		other.link = self
	
		name = "vs2fs_%d" % uid
		uid += 1
	
		self.name  = name
		other.name = name
	
		for field, child in self.fields.iteritems():
			if field in other.fields:
				uid = child.makeLinks(other.fields[field], uid)

		return uid
	
def handleObj(dioa, obj, lut, exist, mask, tobj):
	# Does this field actually exist?
	if mask is dioa.bool.false: return
	
	# Accumulate the mask
	oldmask = tobj.objMasks.get(obj, dioa.bool.false)
	objmask = dioa.bool.or_(oldmask, mask)
	tobj.objMasks[obj] = dioa.set.simplify(exist, objmask, dioa.set.empty)
	
	# Recurse into each of the object's fields
	fieldLUT = obj.slots

	for name, field in fieldLUT.iteritems():
		# Don't ad intrinsic fields to the tree
		if intrinsics.isIntrinsicField(name): continue

		# Don't ad unused fields to the tree
		if field not in lut: continue
		
		# Handle the contents of the field.
		ctree = lut[field].annotation.values.correlated
		handleCTree(dioa, ctree, lut, exist, mask, tobj.getField(name))


def handleCTree(dioa, ctree, lut, exist, mask, tobj):
	ctree = dioa.set.simplify(mask, ctree, dioa.set.empty)
	flat  = dioa.set.flatten(ctree)
	
	for obj in flat:
		# For each possible object, produce a correlated mask
		objleaf = dioa.set.leaf((obj,))
		omask = dioa.bool.in_(objleaf, ctree)
		omask = dioa.bool.and_(mask, omask)
				
		# Recurse
		handleObj(dioa, obj, lut, exist, omask, tobj)


def printNode(tobj):
	print tobj.path
	print tobj.objMasks
	
	for next in tobj.fields.itervalues():
		printNode(next)


def dump(name, tobj):
	print
	print name
	print tobj.treetype		
	printNode(tobj)
	print


# Used for getting the context object.
def getSingleObject(dioa, lut, lcl):
	node = lut[lcl]
	flat  = node.annotation.values.flat
	assert len(flat) == 1
	return tuple(flat)[0]


def evaluateContextObject(dioa, lut, exist, lcl, obj, treetype):
	tobj = IOTreeObj(('context',), treetype)
	tobj.impl = lcl
	
	mask = dioa.bool.true
	handleObj(dioa, obj, lut, exist, mask, tobj)

	if False: dump('context', tobj)

	return tobj


def evaluateLocal(dioa, lut, exist, lcl, treetype):
	if lcl is None: return None
	if lcl.isDoNotCare(): return IOTreeObj((), treetype)
		
	node = lut[lcl]
	
	# The correlated tree
	ctree = node.annotation.values.correlated

	tobj = IOTreeObj((lcl,), treetype)
	tobj.impl = lcl

	handleCTree(dioa, ctree, lut, exist, dioa.bool.true, tobj)
		
	if False: dump(lcl, tobj)
	
	return tobj
