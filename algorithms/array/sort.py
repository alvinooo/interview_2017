def insertion(l):
	for i in xrange(1, len(l)):
		curr = l[i]
		j = i - 1
		while j >= 0 and l[j] > curr:
			l[j + 1] = l[j]
			j -= 1
		l[j + 1] = curr
	return l

def test_insertion():
	print insertion([5,2,4,6,1,3])

test_insertion()

def even_odd_index(l):
	even_ptr, odd_ptr = 0, 1
	while True:
		while even_ptr < len(l) and l[even_ptr] % 2 == 0:
			even_ptr += 1
		while odd_ptr < len(l) and l[odd_ptr] % 2 == 1:
			odd_ptr += 1
		if even_ptr < len(l) and odd_ptr < len(l):
			l[even_ptr], l[odd_ptr] = l[odd_ptr], l[even_ptr]
		else:
			break
	return l

def test_even_odd_index():
	print even_odd_index([2,5,7,8,1,6,9])

# test_even_odd_index()