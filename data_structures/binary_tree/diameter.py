from BTNode import BTNode

def dfs_diameter(tree):
	if not tree:
		return 0, 0
	left_longest, left_diameter = dfs_diameter(tree.left)
	right_longest, right_diameter = dfs_diameter(tree.right)
	return max(left_longest, right_longest) + 1, \
				max(left_longest + 1 + right_longest, \
				left_diameter, right_diameter)

root = BTNode(None)
root.left = BTNode(None)
root.left.left = BTNode(None)
root.left.right = BTNode(None)
root.left.right.right = BTNode(None)
root.right = BTNode(None)
root.right.right = BTNode(None)
root.right.right.right = BTNode(None)
root.right.right.right.left = BTNode(None)
root.right.right.right.left.left = BTNode(None)
root.right.right.right.left.right = BTNode(None)
root.right.right.right.right = BTNode(None)

_, diameter = dfs_diameter(root)
print diameter

root = BTNode(None)
root.left = BTNode(None)
root.left.left = BTNode(None)
root.left.left.left = BTNode(None)
root.left.left.right = BTNode(None)
root.left.left.right.left = BTNode(None)
root.left.left.right.left.left = BTNode(None)
root.left.left.right.left.right = BTNode(None)
root.left.right = BTNode(None)
root.left.right.right = BTNode(None)
root.left.right.right.left = BTNode(None)
root.left.right.right.right = BTNode(None)
root.left.right.right.right.right = BTNode(None)
root.right = BTNode(None)
root.right.right = BTNode(None)

_, diameter = dfs_diameter(root)
print diameter