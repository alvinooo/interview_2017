from BTNode import BTNode

max_len = 0

def longest_increasing_consecutive(root):
	global max_len
	if not root:
		return 0
	len_left = longest_increasing_consecutive(root.left)
	len_right = longest_increasing_consecutive(root.right)
	if root.left:
		if root.value + 1 == root.left.value:
			len_left += 1
		else:
			len_left = 1
	if root.right:
		if root.value + 1 == root.right.value:
			len_right += 1
		else:
			len_right = 1

	max_len = max(max_len, len_left, len_right)
	return max(len_left, len_right, 1)

def test_longest_increasing_consecutive():
	# root = BTNode(6)
	# root.right = BTNode(9)
	# root.right.left = BTNode(7)
	# root.right.right = BTNode(10)
	# root.right.right.right = BTNode(11)
	# longest_increasing_consecutive(root)
	# print max_len

	root = BTNode(1)
	root.left = BTNode(2)
	root.left.left = BTNode(3)
	root.right = BTNode(4)
	root.right.left = BTNode(5)
	root.right.right = BTNode(6)
	root.right.right.left = BTNode(7)
	longest_increasing_consecutive(root)
	print max_len

# test_longest_increasing_consecutive()