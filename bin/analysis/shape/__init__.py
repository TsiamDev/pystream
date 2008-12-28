from __future__ import absolute_import

from _pystream import bijection

# The model for the analysis

from . model import canonical

from . import regionanalysis
from . import transferfunctions
from . import constraintbuilder
from . import dataflow


class RegionBasedShapeAnalysis(object):
	def __init__(self, db):
		self.canonical   = canonical.CanonicalObjects()
		self.worklist    = dataflow.Worklist()
		self.environment = dataflow.DataflowEnvironment()
		
		self.constraintbuilder = constraintbuilder.ShapeConstraintBuilder(self)

		self.db = db


	def process(self):
		self.worklist.process(self)

def evaluate(extractor, entryPoints, adb):
	print "Shape"

	regionLUT = regionanalysis.evaluate(extractor, entryPoints, adb)

	rbsa = RegionBasedShapeAnalysis()
	rbsa.process()
