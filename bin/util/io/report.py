def reindex(indexes, l):
	return [l[i] for i in indexes]


class TableBuilder(object):
	def __init__(self, *columns):
		self.columns = columns
		self.formats = ['%s' for c in columns]

		self.rows = []

	def setFormats(self, *formats):
		assert len(formats) == len(self.columns)
		self.formats = formats

	def row(self, name, *values):
		assert len(values) == len(self.columns)
		self.rows.append((name, values))

	def formatRow(self, name, values):
		return name, [format % value for value, format in zip(values, self.formats)]

	def dump(self):
		for row in self.rows:
			name, data = self.formatRow(*row)
			print name, data

	def rewrite(self, *indexes):
		self.columns = reindex(indexes, self.columns)
		self.formats = reindex(indexes, self.formats)
		self.rows = [(name, reindex(indexes, data)) for name, data in self.rows]


	def dumpLatex(self, f, label):
		print >> f, r"\subfloat[\label{fig:%s}]{" % label
		print >> f, r'\begin{tabular}{|c|%s|}' % "|".join(["c" for name in self.columns])
		print >> f, r'\cline{2-%d}' % (len(self.columns)+1)
		print >> f, r'\multicolumn{1}{c|}{} & %s' % " & ".join([r"\textbf{%s}" %name for name in self.columns])
		print >> f, r'\tabularnewline \hline'

		for row in self.rows:
			name, data = self.formatRow(*row)
			print >> f, r'\textbf{%s} & %s' % (name, " & ".join(data))
			print >> f, r'\tabularnewline \hline'

		print >> f, r'\end{tabular}'
		print >> f, "}"


class PieBuilder(object):
	template = """
#proc getdata
data:
%s

#proc pie
//firstslice: 90
//explode: .2 0 0 0 0  .2 0
datafield: 2
labelfield: 1
labelmode: line+label
//labelmode: labelonly
center: 2 2
radius: 1
colors: %s
labelfarout: 1.3
"""

	def __init__(self):
		self.slices = []

	def slice(self, label, color, value):
		self.slices.append((label, color, value))


	def dumpPloticus(self, f):
		data = "\n".join(["%s %r" % (slice[0], slice[2]) for slice in self.slices])
		colors = " ".join([slice[1] for slice in self.slices])

		print >> f, self.template % (data, colors)
