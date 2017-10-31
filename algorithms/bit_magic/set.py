def set_even_bits(n):
	return 0xAA & n

# print set_even_bits(30)

def count_set_bits(n, left, right):
	n <<= left - 1
	n >>= right - 1
	count = 0
	while n:
		count += n & 1
		n >>= 1
	return count

def test_count_set_bits():
	print count_set_bits(42, 2, 5)
	print count_set_bits(79, 1, 4)

# test_count_set_bits()