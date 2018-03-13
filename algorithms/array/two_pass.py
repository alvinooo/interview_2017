def product_except_self(l):
	products = l[:]
	for i in xrange(1, len(l) - 1):
		products[i] = products[i - 1] * l[i]
	products[len(l) - 1] = products[len(l) - 2]
	curr_product = l[len(l) - 1]
	for i in xrange(len(l) - 2, 0, -1):
		products[i] = curr_product * products[i - 1]
		curr_product = curr_product * l[i]
	products[0] = curr_product
	return products

def test_product_except_self():
	print product_except_self([1,2,3,4])

# test_product_except_self()

def max_j_minus_i(l):
	min_left, max_right = [l[0]], [l[-1]]
	for i in xrange(1, len(l)):
		min_left.append(min(min_left[i - 1], l[i]))
	for i in xrange(len(l) - 2, -1, -1):
		max_right.insert(0, max(max_right[0], l[i]))

	i, j = 0, 0
	max_diff = -1
	while i < len(l) and j < len(l):
		if min_left[i] < max_right[j]:
			max_diff = max(max_diff, j - i)
			j += 1
		else:
			i += 1

	return max_diff

def test_max_j_minus_i():
	print max_j_minus_i([34, 8, 10, 3, 2, 80, 30, 33, 1])
	print max_j_minus_i([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
	print max_j_minus_i([1, 2, 3, 4, 5, 6])
	print max_j_minus_i([6, 5, 4, 3, 2, 1])

# test_max_j_minus_i()