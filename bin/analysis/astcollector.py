from util.typedispatch import *

from language.python import ast
from language.python import program

class GetOps(object):
	__metaclass__ = typedispatcher

	def __init__(self):
		self.ops    = []
		self.locals = set()

	@defaultdispatch
	def default(self, node):
		assert False, repr(node)

	@dispatch(str, type(None), ast.Break, ast.Continue, ast.Code)
	def visitJunk(self, node):
		pass

	@dispatch(ast.Suite, ast.Condition, ast.Assign, ast.Switch, ast.Discard, ast.For, ast.While, ast.CodeParameters)
	def visitOK(self, node):
		visitAllChildren(self, node)

	@dispatch(ast.Local, ast.Existing)
	def visitLocal(self, node):
		self.locals.add(node)

	@dispatch(ast.Load, ast.Store, ast.Check, ast.Allocate, ast.BinaryOp, ast.UnaryPrefixOp,
		  ast.GetGlobal, ast.SetGlobal,
		  ast.GetSubscript, ast.SetSubscript,
		  ast.Call, ast.DirectCall, ast.MethodCall,
		  ast.UnpackSequence,
		  ast.GetAttr, ast.SetAttr,
		  ast.ConvertToBool, ast.Not,
		  ast.BuildTuple, ast.BuildList, ast.GetIter)
	def visitOp(self, node):
		visitAllChildren(self, node)
		self.ops.append(node)

	@dispatch(list, tuple, ast.Return)
	def visitContainer(self, node):
		visitAllChildren(self, node)

	def process(self, node):
		if isinstance(node, ast.Code):
			for child in node.children():
				self(child)
		else:
			node.collectNodes(self)

		return self.ops, self.locals


def getOps(func):
	go = GetOps()
	go.process(func)
	return go.ops, go.locals
