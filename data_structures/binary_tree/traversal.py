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