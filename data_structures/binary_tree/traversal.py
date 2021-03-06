from BTNode import BTNode
from collections import deque

def reverse_level_order(root):
	s = []
	q = deque()
	q.append(root)
	while q:
		curr = q.popleft()
		if curr.right:
			q.append(curr.right)
		if curr.left:
			q.append(curr.left)
		s.append(curr)
	while s:
		print s.pop().value

def test_reverse_level_order():
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	reverse_level_order(root)

# test_reverse_level_order()

def product_of_leaves(root):
	q = deque()
	q.append(root)
	product = 1
	while q:
		curr_sum, level_size = 0, len(q)
		for i in xrange(level_size):
			curr_node = q.popleft()
			if not curr_node.left and not curr_node.right:
				curr_sum += curr_node.value
			if curr_node.left:
				q.append(curr_node.left)
			if curr_node.right:
				q.append(curr_node.right)
		if curr_sum > 0:
			product *= curr_sum
	return product

def test_product_of_leaves():
	root = BTNode(2)
	root.left = BTNode(7)
	root.right = BTNode(5)
	root.right.right = BTNode(9)
	print product_of_leaves(root)

	root = BTNode(2)
	root.left = BTNode(7)
	root.left.left = BTNode(8)
	root.left.right = BTNode(6)
	root.left.right.left = BTNode(1)
	root.left.right.right = BTNode(11)
	root.right = BTNode(5)
	root.right.right = BTNode(9)
	root.right.right.left = BTNode(4)
	root.right.right.right = BTNode(10)
	print product_of_leaves(root)

# test_product_of_leaves()

def left_to_right_leaves(root):
	if root:
		if not root.left and not root.right:
			print root.value
		else:
			left_to_right_leaves(root.left)
			left_to_right_leaves(root.right)

def test_left_to_right_leaves():
	root = BTNode(1)
	root.left = BTNode(2)
	root.left.left = BTNode(4)
	root.right = BTNode(3)
	root.right.left = BTNode(5)
	root.right.left.left = BTNode(6)
	root.right.left.right = BTNode(7)
	root.right.right = BTNode(8)
	root.right.right.left = BTNode(9)
	root.right.right.right = BTNode(10)
	left_to_right_leaves(root)

# test_left_to_right_leaves()

def most_nodes_level(root):
	max_nodes, max_level, curr_level = 0, 1, 1
	q = deque()
	q.append(root)
	while q:
		len_q = len(q)
		if len_q > max_nodes:
			max_nodes, max_level = len_q, curr_level
		for i in xrange(len_q):
			node = q.popleft()
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		curr_level += 1
	return max_level

def test_most_nodes_level():
	root = BTNode(2)
	root.left = BTNode(1)
	root.left.left = BTNode(4)
	root.left.right = BTNode(6)
	root.left.right.left = BTNode(5)
	root.right = BTNode(3)
	root.right.right = BTNode(8)
	print most_nodes_level(root)

# test_most_nodes_level()

def spiral(root):
	zig = [root]
	zag = []
	while zig or zag:
		while zag:
			curr = zag.pop()
			if curr.right:
				zig.append(curr.right)
			if curr.left:
				zig.append(curr.left)
			print curr.value,
		while zig:
			curr = zig.pop()
			if curr.left:
				zag.append(curr.left)
			if curr.right:
				zag.append(curr.right)
			print curr.value,

def test_spiral():
	# root = BTNode(1)
	# root.left = BTNode(2)
	# root.right = BTNode(3)
	# root.left.left = BTNode(7)
	# root.left.right = BTNode(6)
	# root.right.left = BTNode(5)
	# root.right.right = BTNode(4)
	root = BTNode(3)
	root.left = BTNode(9)
	root.right = BTNode(20)
	root.right.left = BTNode(15)
	root.right.right = BTNode(7)
	spiral(root)

# test_spiral()

def sum_paths(root, value=0):
	if not root:
		return 0
	curr_sum = value * 10 + root.value
	if not root.left and not root.right:
		print curr_sum
		return curr_sum
	return sum_paths(root.left, curr_sum) + sum_paths(root.right, curr_sum)

def test_sum_paths():
	root = BTNode(6)
	root.left = BTNode(3)
	root.left.left = BTNode(2)
	root.left.right = BTNode(5)
	root.left.right.left = BTNode(7)
	root.left.right.right = BTNode(4)
	root.right = BTNode(5)
	root.right.right = BTNode(4)
	print sum_paths(root)

# test_sum_paths()

def iterative_pre_order(root):
	s = [root]
	while s:
		curr = s.pop()
		print curr.value,
		if curr.right:
			s.append(curr.right)
		if curr.left:
			s.append(curr.left)

def test_iterative_pre_order():
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	root.right.left = BTNode(6)
	root.right.right = BTNode(7)
	iterative_pre_order(root) # 4, 5, 2, 6, 7, 3, 1
	print

# test_iterative_pre_order()

def iterative_in_order(root):
	curr = root
	s = [root]
	left_visited = False
	while s:
		while curr.left and not left_visited:
			s.append(curr.left)
			curr = curr.left
		left_visited = True
		curr = s.pop()
		print curr.value,
		if curr.right:
			s.append(curr.right)
			curr = curr.right
			left_visited = False

def test_iterative_in_order():
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	root.right.left = BTNode(6)
	root.right.right = BTNode(7)
	iterative_in_order(root) # 4, 5, 2, 6, 7, 3, 1
	print

# test_iterative_in_order()

def iterative_post_order_two_stacks(root):
	curr_stack = [root]
	processed = []
	while curr_stack:
		curr = curr_stack.pop()
		if curr.left:
			curr_stack.append(curr.left)
		if curr.right:
			curr_stack.append(curr.right)
		processed.append(curr)
	while processed:
		print processed.pop().value,

def iterative_post_order_one_stack(root):
	stack = [root]
	parent = None
	while stack:
		curr = stack[-1]
		if not curr.left and not curr.right or curr == parent:
			stack.pop()
		else:
			parent = curr
			if curr.right:
				stack.append(curr.right)
			if curr.left:
				stack.append(curr.left)

def test_iterative_post_order():
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	root.right.left = BTNode(6)
	root.right.right = BTNode(7)
	iterative_post_order_two_stacks(root) # 4, 5, 2, 6, 7, 3, 1
	print

# test_iterative_post_order()

# TODO morris traversal

def lca(root, n1, n2):
	if not root:
		return None
	if root == n1 or root == n2:
		return root
	left = lca(root.left, n1, n2)
	right = lca(root.right, n1, n2)
	if left and right:
		return root
	return left if left else right

def lca_bst(root, n1, n2):
	if not root:
		return None
	elif n1.value < root.value and n2.value < root.value:
		return lca_bst(root.left, n1, n2)
	elif n1.value > root.value and n2.value > root.value:
		return lca_bst(root.right, n1, n2)
	else:
		return root

def test_lca():
	root = BTNode(1)
	root.left = BTNode(2)
	root.right = BTNode(3)
	root.left.left = BTNode(4)
	root.left.right = BTNode(5)
	root.right.left = BTNode(6)
	root.right.right = BTNode(7)
	print lca(root, root.left.left, root.left.right).value
	print lca(root, root.left.left, root.right.left).value
	print lca(root, root.right, root.left.left).value
	print lca(root, root.left, root.left.left).value

	root = BTNode(20)
	root.left = BTNode(8)
	root.left.left = BTNode(4)
	root.left.right = BTNode(12)
	root.left.right.left = BTNode(10)
	root.left.right.right = BTNode(14)
	root.right = BTNode(22)

	print lca_bst(root, root.left.right.left, root.left.right.right).value
	print lca_bst(root, root.left.right.right, root.left.left).value
	print lca_bst(root, root.left.right.left, root.right).value

test_lca()