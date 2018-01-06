class BTNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)

class BSTNode(BTNode):

	def insert_value(self, value):
		self._insert(self, BSTNode(value))

	def insert_node(self, node):
		self._insert(self, node)

	def _insert(self, root, node):
		if not root:
			return node
		if node.value < root.value:
			root.left = self._insert(root.left, node)
		elif node.value > root.value:
			root.right = self._insert(root.right, node)
		return root

	def in_order_traversal(self, root):
		if root:
			self.in_order_traversal(root.left)
			print root.value,
			self.in_order_traversal(root.right)

	def pre_order_traversal(self, root):
		if root:
			print root.value,
			self.pre_order_traversal(root.left)
			self.pre_order_traversal(root.right)

	def post_order_traversal(self, root):
		if root:
			self.post_order_traversal(root.left)
			self.post_order_traversal(root.right)
			print root.value,

if __name__ == "__main__":
	t = BSTNode(4)
	for i in [2, 6, 1, 3, 5, 7]:
		t.insert_value(i)
	t.in_order_traversal(t)