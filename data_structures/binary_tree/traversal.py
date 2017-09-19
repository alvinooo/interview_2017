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

reverse_level_order(root)