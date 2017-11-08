from collections import deque

def bfs(g, start_row, start_column, visited):
	cells_visited = 0
	q = deque()
	if g[start_row][start_column] == 1:
		q.append((start_row, start_column))
	while q:
		row, column = q.popleft()
		if visited[row][column]:
			continue
		visited[row][column] = 1
		cells_visited += 1
		if row > 0 and g[row - 1][column] == 1:
			q.append((row - 1, column))
		if row < len(g) - 1 and g[row + 1][column] == 1:
			q.append((row + 1, column))
		if column > 0 and g[row][column - 1] == 1:
			q.append((row, column - 1))
		if column < len(g[0]) - 1 and g[row][column + 1] == 1:
			q.append((row, column + 1))
	return 1 if cells_visited > 0 else 0

def count_islands(g):
	islands = 0
	visited = [[0 for _ in g[0]] for _ in g]
	for row in xrange(len(g)):
		for column in xrange(len(g[row])):
			islands += bfs(g, row, column, visited)
	return islands

def test_count_islands():
	print count_islands(
		[
			[1,1,1,1,0],
			[1,1,0,1,0],
			[1,1,0,0,0],
			[0,0,0,0,0]
		]
	)
	print count_islands(
		[
			[1,1,0,0,0],
			[1,1,0,0,0],
			[0,0,1,0,0],
			[0,0,0,1,1]
		]
	)

# test_count_islands()

# TODO union find?