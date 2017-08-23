from BTNode import BTNode

def dfs_diameter(tree):
	if not tree:
		return 0
	left_longest, left_diameter = dfs_diameter(tree.left)
	right_longest, right_diameter = dfs_diameter(tree.right)
	return max(left_longest, right_longest) + 1,
			max(left_longest + 1 + right_longest,
				left_diameter, right_diameter)

root = BTNode(None)
root.left = BTNode(None)
root.left.left = BTNode(None)
root.left.right = BTNode(None)
root.left.right.right = BTNode(None)