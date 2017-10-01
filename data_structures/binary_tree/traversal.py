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

root = BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)
root.left.left = BTNode(4)
root.left.right = BTNode(5)

# reverse_level_order(root)

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

root = BTNode(2)
root.left = BTNode(7)
root.right = BTNode(5)
root.right.right = BTNode(9)

# print product_of_leaves(root)

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

# print product_of_leaves(root)

def left_to_right_leaves(root):
	if root:
		if not root.left and not root.right:
			print root.value
		else:
			left_to_right_leaves(root.left)
			left_to_right_leaves(root.right)

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

# left_to_right_leaves(root)

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

root = BTNode(2)
root.left = BTNode(1)
root.left.left = BTNode(4)
root.left.right = BTNode(6)
root.left.right.left = BTNode(5)
root.right = BTNode(3)
root.right.right = BTNode(8)

print most_nodes_level(root)