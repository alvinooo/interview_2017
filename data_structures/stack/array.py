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

test_nge()

def is_valid_preorder(l):
	if len(l) <= 1:
		return True
	border = 1
	while border < len(l) and l[border] < l[0]:
		border += 1
	if not all(map(lambda x: x > l[0], l[border:])):
		return False
	return is_valid_preorder(l[1:border]) and is_valid_preorder(l[border:])

"""
	_
root		=> Return False
		_
"""
def is_valid_preorder_stack(l):
	# Process left subtree
	# If element is less than root return False
	pass

def test_is_valid_preorder():
	print is_valid_preorder([2,4,3])
	print is_valid_preorder([2,4,1])
	print is_valid_preorder([40,30,35,80,100])
	print is_valid_preorder([40,30,35,20,80,100])

# test_is_valid_preorder()