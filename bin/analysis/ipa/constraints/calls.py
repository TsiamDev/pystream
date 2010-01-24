from .. calling import cpa, transfer, callbinder
from . import node

class AbstractCall(object):
	def __init__(self):
		self.dirty = False
		self.cache = {}

def argIsOK(arg):
	return arg is None or isinstance(arg, node.ConstraintNode)

class CallConstraint(AbstractCall):
	def __init__(self, context, op, selfarg, args, kwds, varg, karg, targets):
		AbstractCall.__init__(self)
		self.context = context
		self.op = op
		self.selfarg = selfarg
		self.args = args
		self.kwds = kwds
		self.varg = varg
		self.karg = karg
		self.targets = targets

		self.selfarg.attachExactSplit(self.splitChanged)

	def splitChanged(self):
		if not self.dirty:
			self.dirty = True
			self.context.dirtyCall(self)

	def __repr__(self):
		return "[CALL %r(%r, %r, *%r, **%r) -> %r]" % (self.selfarg, self.args, self.kwds, self.varg, self.karg, self.targets)

	def resolve(self, context):
		self.dirty = False

		selfsplit = self.selfarg.exactSplit

		for selfobj, selflcl in selfsplit.objects.iteritems():
			# TODO prevent over splitting?  DN objects are dealt with separately from HZ objects.
			key = selfobj
			if key not in self.cache:
				self.cache[key] = None

				code = context.analysis.getCode(selfobj)

				context.dcall(self.op, code, selflcl, self.args, self.kwds, self.varg, self.karg, self.targets)

class DirectCallConstraint(AbstractCall):
	def __init__(self, context, op, code, selfarg, args, kwds, varg, karg, targets):
		assert code is not None
		assert argIsOK(selfarg), selfarg
		AbstractCall.__init__(self)
		self.context = context
		self.op = op
		self.code = code
		self.selfarg = selfarg
		self.args = args
		self.kwds = kwds
		self.varg = varg
		self.karg = karg
		self.targets = targets

		assert isinstance(varg, node.ConstraintNode), varg

		# TODO no need for the split locals?
		self.varg.attachExactSplit(self.splitChanged)

	def splitChanged(self):
		if not self.dirty:
			self.dirty = True
			self.context.dirtyDCall(self)

	def __repr__(self):
		return "[DCALL %s %r(%r, %r, *%r, **%r) -> %r]" % (self.code, self.selfarg, self.args, self.kwds, self.varg, self.karg, self.targets)

	def vargObjSlots(self, vargObj):
		slots = []

		if vargObj is None: return slots

		analysis = self.context.analysis

		lengthSlot = self.context.field(vargObj, 'LowLevel', analysis.pyObj('length'))
		assert len(lengthSlot.values) == 1
		length = tuple(lengthSlot.values)[0].xtype.obj.pyobj


		for i in range(length):
			slot = self.context.field(vargObj, 'Array', analysis.pyObj(i))
			slots.append(slot)

		return slots

	def resolve(self, context):
		self.dirty = False

		assert self.varg

		for vargObj in self.varg.exactSplit.objects.iterkeys():
			key = vargObj
			if key not in self.cache:
				self.cache[key] = None

				vargSlots = self.vargObjSlots(vargObj)
				context.fcall(self.op, self.code, self.selfarg, self.args, self.kwds, vargSlots, self.karg, self.targets)


class FlatCallConstraint(AbstractCall):
	def __init__(self, context, op, code, selfarg, args, kwds, varg, karg, targets):
		assert argIsOK(selfarg), selfarg
		assert isinstance(varg, list), varg

		assert not kwds
		assert karg is None

		AbstractCall.__init__(self)
		self.context = context
		self.op = op
		self.code = code
		self.selfarg = selfarg
		self.args = args
		self.kwds = kwds
		self.varg = varg
		self.karg = karg
		self.targets = targets

		self.info = transfer.computeTransferInfo(self.code, self.selfarg is not None, len(self.args), len(self.varg))

		if self.info.maybeOK():
			if self.selfarg is not None:
				self.selfarg.attachTypeSplit(self.splitChanged)

			for arg in args:
				arg.attachTypeSplit(self.splitChanged)

			for arg in varg:
				arg.attachTypeSplit(self.splitChanged)
		else:
			import pdb
			pdb.set_trace()

	def splitChanged(self):
		if not self.dirty:
			self.dirty = True
			self.context.dirtyFCall(self)

	def __repr__(self):
		return "[FCALL %s %r(%r, %r, *%r, **%r) -> %r]" % (self.code, self.selfarg, self.args, self.kwds, self.varg, self.karg, self.targets)

	def resolve(self, context):
		self.dirty = False

		info = self.info
		ctsb = cpa.CPATypeSigBuilder(context.analysis, self, info)
		info.transfer(ctsb, ctsb)
		sigs = ctsb.signatures()

		for sig in sigs:
			if not sig in self.cache:
				print sig

				# HACK - varg can be weird, must take it into account?
				self.cache[sig] = None

				invoked = context.analysis.getContext(sig)
				callbinder.bind(self, invoked, info)