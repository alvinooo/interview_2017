# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
import sys, os
sys.path.append(os.path.abspath('../../data_structures/trie'))
from Trie import Trie

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

def dfs_with_trie(row, col, grid, curr_node, found_words, visited=None, curr_path=None):
	if not visited:
		visited = [[False for c in r] for r in grid]
	if not curr_path:
		curr_path = []
	if curr_node.end:
		found_words.add(''.join(curr_path))
	next_node = curr_node.keys[ord(grid[row][col]) - ord('a')]
	if not visited[row][col] and next_node:
		visited[row][col] = True
		curr_path.append(grid[row][col])
		if row > 0:
			dfs_with_trie(row - 1, col, grid, next_node, found_words, visited, curr_path)
		if row < len(grid) - 1:
			dfs_with_trie(row + 1, col, grid, next_node, found_words, visited, curr_path)
		if col > 0:
			dfs_with_trie(row, col - 1, grid, next_node, found_words, visited, curr_path)
		if col < len(grid[0]) - 1:
			dfs_with_trie(row, col + 1, grid, next_node, found_words, visited, curr_path)
		curr_path.pop()
	visited[row][col] = False

def word_search_ii(grid, words):
	dictionary = Trie(map(chr, xrange(97, 123)))
	for word in words:
		dictionary.add(word)

	found_words = set()
	for row in xrange(len(grid)):
		for col in xrange(len(grid[0])):
			dfs_with_trie(row, col, grid, dictionary.root, found_words)
	return found_words

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

	lower_grid = [
					['o','a','a','n'],
					['e','t','a','e'],
					['i','h','k','r'],
					['i','f','l','v']
				]

	print word_search_ii(lower_grid, ["oath","pea","eat","rain", "oaaa"])

test_word_search()