class ReversePostorderCrawler(object):
	def __init__(self, G, head):
		self.G = G
		self.head = head

		self.processed = set()
		self.order = []
		self(head)
		self.order.reverse()
			
	def __call__(self, node):
		self.processed.add(node)
		for next in self.G.get(node, ()):
			if next not in self.processed:
				self(next)
		self.order.append(node)



def intersect(doms, b1, b2):
	finger1 = b1
	finger2 = b2
	while finger1 != finger2:
		while finger1 > finger2:
			finger1 = doms[finger1]
			
		while finger2 > finger1:
			finger2 = doms[finger2]
	return finger1

def dominatorTree(G, head):
	order = ReversePostorderCrawler(G, head).order

	# Make forward and reverse maps G <-> reverse postorder
	forward = {}
	reverse = {}
	for i, node in enumerate(order):
		forward[node] = i
		reverse[i] = node
		
	
	# Find the predicesors, in reverse postorder space.
	pred = {}
	for node, nexts in G.iteritems():
		i = forward[node]
		for next in nexts:
			n = forward[next]

			# Eliminate self-cycles.
			if i == n: continue

			if n not in pred:
				pred[n] = [i]
			else:
				pred[n].append(i)

	# Setup for calculation
	count = len(order)
	doms = [None for i in range(count)]

	# Special case the head
	doms[0] = 0

	# Calculate a fixedpoint solution
	changed = True
	while changed:
		changed = False
		for node in range(1, count):
			# Find an inital value for the immediate dominator
			if doms[node] is None:
				new_idom = min(pred[node])
				assert new_idom < node
			else:
				new_idom = doms[node]

			# Refine the immediate dominator,
			# make it consistant with the predicesors.
			for p in pred[node]:
				if doms[p] is not None:			
					new_idom = intersect(doms, new_idom, p)

			# Check if the immediate dominator has changed.
			if doms[node] is not new_idom:
				assert doms[node] is None or new_idom < doms[node]
				doms[node] = new_idom
				changed = True


	# Map the solution onto the original graph.
	idoms = {}
	tree  = {}
	for node, idom in enumerate(doms):
		if node is 0: continue # Skip the head
		node = reverse[node]
		idom = reverse[idom]
		idoms[node] = idom

		if idom not in tree:
			tree[idom] = [node]
		else:
			tree[idom].append(node)
	return tree
	
def reverseGraph(G):
	out = {}
	for node, nexts in G.iteritems():
		for next in nexts:
			if next not in out:
				out[next] = [node]
			else:
				out[next].append(node)
	return out

def makeSingleHead(G, head):
	entryPoints = findEntryPoints(G)
	G[head] = entryPoints

def findEntryPoints(G):
	entryPoints = set(G.iterkeys())
	for nexts in G.itervalues():
		for next in nexts:
			if next in entryPoints:
				entryPoints.remove(next)
	return list(entryPoints)

if __name__ == '__main__':
	G = {0:(1, 2), 1:(3,), 2:(3,), 3:(4, 5), 4:(6,), 5:(6,)}

	head = None
	makeSingleHead(G, head)
	print dominatorTree(G, head)
