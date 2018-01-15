# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

def dfs(row, col, grid, word, index=0, visited=None):
	if not visited:
		visited = [[False for c in r] for r in grid]
	if index == len(word):
		return True
	if not visited[row][col] and grid[row][col] == word[index]:
		visited[row][col] = True
		up = row > 0 and dfs(row - 1, col, grid, word, index + 1, visited)
		down = row < len(grid) - 1 and dfs(row + 1, col, grid, word, index + 1, visited)
		left = col > 0 and dfs(row, col - 1, grid, word, index + 1, visited)
		right = col < len(grid[0]) - 1 and dfs(row, col + 1, grid, word, index + 1, visited)
		if up or down or left or right:
			return True
	visited[row][col] = False
	return False

def word_search(grid, word):
	for row in xrange(len(grid)):
		for col in xrange(len(grid[0])):
			if dfs(row, col, grid, word):
				return True
	return False

def test_word_search():
	grid = 	[
			  ['A','B','C','E'],
			  ['S','F','C','S'],
			  ['A','D','E','E']
			]
	print word_search(grid, "ABCCED")
	print word_search(grid, "SEE")
	print word_search(grid, "ABCB")
	print word_search(grid, "ABCESEEDASFCS")

test_word_search()