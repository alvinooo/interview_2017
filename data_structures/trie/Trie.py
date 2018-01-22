class TrieNode(object):
	def __init__(self, end=False, keys=[]):
		self.end = end
		self.keys = [None for _ in keys]

class Trie(object):
	def __init__(self, keys=[]):
		self.root = TrieNode(keys=keys)
		self.keys = keys

	def add(self, word):
		curr = self.root
		for letter_index in xrange(len(word)):
			key_index = ord(word[letter_index]) - ord(self.keys[0])
			if not curr.keys[key_index]:
				curr.keys[key_index] = TrieNode(keys=self.keys)
			if letter_index < len(word) - 1:
				curr = curr.keys[key_index]
			else:
				curr.keys[key_index].end = True

	def find(self, word, prefix=False):
		curr = self.root
		for letter in word:
			key_index = ord(letter) - ord(self.keys[0])
			if not curr.keys[key_index]:
				return False
			curr = curr.keys[key_index]
		return curr.end or prefix

	def find_debug(self, word):
		curr_node, curr_letter = self.root, ''
		for letter in word:
			key_index = ord(letter) - ord(self.keys[0])
			if not curr_node.keys[key_index]:
				return False, letter
			curr_node = curr_node.keys[key_index]
		return curr_node.end, curr_letter

	def list(self):
		self._list_helper(self.root)

	def _list_helper(self, root, prefix=''):
		if root.end:
			print prefix
		for index in xrange(len(root.keys)):
			letter, ptr = chr(index + ord(self.keys[0])), root.keys[index]
			if ptr:
				self._list_helper(ptr, prefix=prefix+letter)

if __name__ == "__main__":
	trie = Trie(keys=map(chr, xrange(97, 123)))
	trie.add('a')
	trie.add('ab')
	trie.add('abc')
	trie.add('b')
	trie.add('bc')
	trie.add('bcde')
	trie.list()
	print trie.find('')
	print trie.find('bc')
	print trie.find('bcd')

	print trie.find_debug('ad')
	print trie.find('bcd', prefix=True)