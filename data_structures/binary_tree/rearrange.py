from BTNode import BSTNode

# https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge

# TODO merge

def split_at_n(root, n):
	if not root:
		return None, None
	if root.value >= n:
		root_le, root_g = split_at_n(root.left, n)
		root_le.
		return root_le, root_g
	else:
		root_g, root_g = split_at_n(root.right, n)
		return root_le, root_g

def test_split_at_n():
	root = BSTNode(50)
	root.insert_value(40)
	root.insert_value(60)
	root.insert_value(30)
	root.insert_value(45)
	root.insert_value(55)
	root.insert_value(58)
	# root.in_order_traversal(root)
	# print
	# root.pre_order_traversal(root)
	# print
	# root.post_order_traversal(root)
	root_le, root_g = split_at_n(root=root, n=50)
	print root_le, root_g
	root_le.pre_order_traversal(root_le)
	print
	root_g.pre_order_traversal(root_g)

# test_split_at_n()