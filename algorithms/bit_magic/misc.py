def pair_bit_diff(l):
	diff = 0
	for bit in xrange(32):
		num_set_bits = 0
		for num in l:
			if num & (1 << bit):
				num_set_bits += 1
		diff += 2 * num_set_bits * (len(l) - num_set_bits)
	return diff

print pair_bit_diff([1,3,6])