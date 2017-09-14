from BTNode import BTNode

def is_full(root):
	if not root or not root.left and not root.right:
		return True
	elif root.left and root.right:
		return is_full(root.left) and is_full(root.right)
	else:
		return False

tree_1 = BTNode(None)
tree_1.left = BTNode(None)
tree_1.left.left = BTNode(None)
tree_1.left.right = BTNode(None)
tree_1.right = BTNode(None)

print is_full(tree_1)

tree_2 = BTNode(None)
tree_2.left = BTNode(None)
tree_2.left.left = BTNode(None)
tree_2.right = BTNode(None)

print is_full(tree_2)