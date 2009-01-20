from __future__ import absolute_import
import unittest

import analysis.cpa
from decompiler.programextractor import Extractor
from util import replaceGlobals

class TestCPA(unittest.TestCase):
	def assertIn(self, first, second, msg=None):
		"""Fail if the one object is not in the other, using the "in" operator.
		"""
		if first not in second:
			raise self.failureException, (msg or '%r not in %r' % (first, second))


	def assertLocalRefTypes(self, finfo, lcl, types):
		self.assertIn(lcl, finfo.localInfos)
		linfo  = finfo.localInfos[lcl].merged
		refs   = linfo.references

		# There's one reference returned, and it's an integer.
		self.assertEqual(len(refs), len(types))
		for ref in refs:
			self.assertIn(ref.obj.type, types)


	def processFunc(self, func):

		func = replaceGlobals(func, {})

		funcobj = self.extractor.getObject(func)

		self.extractor.ensureLoaded(funcobj)
		funcast = self.extractor.getCall(funcobj)
	
		return func, funcast, funcobj


	def testAdd(self):
		self.extractor = Extractor(verbose=False)
		
		def func(a, b):
			return 2*a+b

		func, funcast, funcobj = self.processFunc(func)

		for paramname in funcast.code.parameternames:
			self.assertEqual(type(paramname), str)
		
		a = self.extractor.getObject(3)
		b = self.extractor.getObject(5)

		result = analysis.cpa.evaluate(self.extractor, [(funcast, funcobj, (a, b))])

		finfo  = result.db.functionInfo(funcast)
		types = set((self.extractor.getObject(int),))

		for param in funcast.code.parameters:
			self.assertLocalRefTypes(finfo, param, types)
			
		self.assertLocalRefTypes(finfo, funcast.code.returnparam, types)