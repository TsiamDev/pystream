from application.makefile import Makefile

def pystreamCompile(filename):
	mf = Makefile(filename)
	mf.pystreamCompile()
