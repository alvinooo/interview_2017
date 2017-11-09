class GNode(object):
	def __init__(self, value):
		self.value = value
		self.neighbors = set()

class Graph(object):

	def __init__(self, edges):
		self.nodes = self.build_graph(edges)

	def build_graph(self, edges):
		"""edges = [('a', 'b'), ('b', 'a'), ...}"""
		nodes = {value: GNode(value) for value in zip(*edges)[0] + zip(*edges)[1]}
		for edge in edges:
			src, dest = edge
			if src not in nodes:
				nodes[src] = GNode(src)
			if dest not in nodes:
				neighbor = GNode(dest)
				nodes[dest] = neighbor
			else:
				neighbor = nodes[dest]
			nodes[src].neighbors.add(neighbor)
		return nodes.values()

	def __str__(self):
		return ','.join([str(n.value) for n in self.nodes])