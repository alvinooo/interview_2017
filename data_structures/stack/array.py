def nge(l):
	s = []
	for item in l:
		while s and item > s[-1]:
			print s.pop(), item
		s.append(item)
	while s:
		print s.pop(), -1
	print

def test_nge():
	nge([4,5,2,25])
	nge([13,7,6,12])

# test_nge()

def is_valid_preorder(l):
	if len(l) <= 1:
		return True
	border = 1
	while border < len(l) and l[border] < l[0]:
		border += 1
	if not all(map(lambda x: x > l[0], l[border:])):
		return False
	return is_valid_preorder(l[1:border]) and is_valid_preorder(l[border:])

def is_valid_preorder_stack(l):
	root = min(l)
	s = []
	for node in l:
		if root > node:
			return False
		while s and node > s[-1]:
			root = s.pop()
		s.append(node)
	return True

def test_is_valid_preorder():
	print is_valid_preorder([2,4,3])
	print is_valid_preorder([2,4,1])
	print is_valid_preorder([40,30,35,80,100])
	print is_valid_preorder([40,30,35,20,80,100])

	print is_valid_preorder_stack([2,4,3])
	print is_valid_preorder_stack([2,4,1])
	print is_valid_preorder_stack([40,30,35,80,100])
	print is_valid_preorder_stack([40,30,35,20,80,100])

# test_is_valid_preorder()