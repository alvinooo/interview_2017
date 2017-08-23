class BTNode(object):
	def __init__(self, value):

		self.value = value
		self.left = None
		self.right = None

class BSTNode(BTNode):

	def insert_value(self, value):
		self._insert(self, BTNode(value))

	def insert_node(self, node):
		self._insert(self, node)

	def _insert(self, root, node):
		if not root:
			return node
		if node.value < root.value:
			root.left = self._insert(root.left, node)
		if node.value > root.value:
			root.right = self._insert(root.right, node)
		return root

	def in_order_traversal(self, root):
		if root:
			self.in_order_traversal(root.left)
			print root.value
			self.in_order_traversal(root.right)

if __name__ == "__main__":
	t = BSTNode(4)
	for i in [2, 6, 1, 3, 5, 7]:
		t.insert_value(i)
	t.in_order_traversal(t)