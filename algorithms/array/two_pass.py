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

# http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/