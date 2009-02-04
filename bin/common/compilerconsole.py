import sys
import time
import util

class Scope(object):
	def __init__(self, parent, name):
		self.parent   = parent
		self.name     = name
		self.children = []

	def begin(self):
		self._start = time.clock()

	def end(self):
		self._end = time.clock()

	@property
	def elapsed(self):
		return self._end-self._start

	def path(self):
		if self.parent is None:
			return ()
		else:
			return self.parent.path()+(self.name,)

	def child(self, name):
		return Scope(self, name)





class CompilerConsole(object):
	def __init__(self, out=None):
		if out is None:
			out = sys.stdout
		self.out = out

		self.root = Scope(None, 'root')
		self.current = self.root

		self.blameOutput  = False

	def path(self):
		return "[ %s ]" % " | ".join(self.current.path())

	def begin(self, name):
		scope = self.current.child(name)
		scope.begin()
		self.current = scope

		self.output("begin %s" % self.path(), 0)

	def end(self):
		self.current.end()
		self.output("end   %s %s" % (self.path(), util.elapsedTimeString(self.current.elapsed)), 0)
		self.current = self.current.parent

	def blame(self):
		caller = sys._getframe(2)
		globals = caller.f_globals
		lineno = caller.f_lineno

		#filename = globals.get('__file__')
		filename = caller.f_code.co_filename
		return "%s:%d" % (filename, lineno)

	def output(self, s, tabs=1):
		if tabs:
			self.out.write('\t'*tabs)

		if self.blameOutput and tabs:
			self.out.write(self.blame()+" ")


		self.out.write(s)
		self.out.write('\n')