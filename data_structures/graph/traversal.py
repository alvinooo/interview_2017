from Graph import Graph

def stack_dfs(g):
	s = [g.nodes[0]]
	visited = {node.value: False for node in g.nodes}
	while s:
		node = s.pop()
		if not visited[node.value]:
			visited[node.value] = True
			print node.value,
		for neighbor in reversed(list(node.neighbors)):
			if not visited[neighbor.value]:
				s.append(neighbor)

def test_stack_dfs():
	edges = [(0, 1), (1, 2), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4)]
	g = Graph(edges)
	stack_dfs(g)
	print

test_stack_dfs()