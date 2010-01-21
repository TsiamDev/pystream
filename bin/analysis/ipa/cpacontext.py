import itertools

from util import canonical

class CPAContextSignature(canonical.CanonicalObject):
	def __init__(self, code, selfparam, params, vparams):
		self.code      = code
		self.selfparam = selfparam
		self.params    = params
		self.vparams   = vparams

		# Sanity check, probably a runaway loop in the analysis logic.
		assert len(vparams) < 30, code

		self.setCanonical(code, selfparam, params, vparams)

	def __repr__(self):
		return "cpa(%r, %r, %r, %r)" % (self.code, self.selfparam, self.params, self.vparams)

anyType = object()
anyTypeIter = (anyType,)
nullIter = (None,)

class CPATypeSigBuilder(object):
	def __init__(self, analysis, call, info):
		self.analysis = analysis
		self.call = call

		self.code = self.call.code
		self.selfparam  = set()
		self.params     = [set() for i in range(info.numParams())]
		self.vparams    = [set() for i in range(info.numVParams())]

		if call.selfarg is None:
			self.selfparam = nullIter

		assert not info.numKParams()

	def setSelfParam(self, value):
		self.selfparam.update(value)

	def setParam(self, index, value):
		self.params[index].update(value)

	def setVParam(self, index, value):
		self.vparams[index].update(value)

	def getSelfArg(self):
		return self.call.selfarg.objs

	def getArg(self, index):
		return self.call.args[index].objs

	def getVArg(self, index):
		return self.call.vargTemp[index].objs

	def convertMegamorphic(self):
		# selfparam should NOT be megamorphic... preserve the precision of method dispatch
#		if len(self.selfparam) > 4:
#			self.selfparam = anyTypeIter

		for i, values in enumerate(self.params):
			if len(values) > 4:
				self.params[i] = anyTypeIter

		for i, values in enumerate(self.vparams):
			if len(values) > 4:
				self.vparams[i] = anyTypeIter


	def signatures(self):
		self.convertMegamorphic()

		results = []

		for concrete in itertools.product(self.selfparam, *self.params+self.vparams):
			selfparam = concrete[0]
			params = concrete[1:len(self.params)+1]
			vparams = concrete[len(self.params)+1:]

			results.append(CPAContextSignature(self.code, selfparam, params, vparams))

		return results

externalContext = CPAContextSignature(None, None, (), ())