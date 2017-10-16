def max_non_adjacent_sum(l):
	if len(l) == 0:
		return 0
	elif len(l) == 1:
		return l[0]
	sums = [0 for _ in l]
	sums[0] = l[0]
	sums[1] = max(l[0], l[1])
	for i in xrange(2, len(l)):
		sums[i] = max(sums[i - 2] + l[i], sums[i - 1])
	return sums[-1]

def max_non_adjacent_sum_constant_space(l):
	if len(l) == 0:
		return 0
	elif len(l) == 1:
		return l[0]
	excl, incl = l[0], l[1]
	for i in xrange(2, len(l)):
		excl, incl = max(excl, incl), excl + l[i]
	return max(excl, incl)

def test_max_non_adjacent_sum():
	print max_non_adjacent_sum([5, 5, 10, 100, 10, 5])
	print max_non_adjacent_sum([1, 2, 3])
	print max_non_adjacent_sum([1, 20, 3])
	print max_non_adjacent_sum_constant_space([5, 5, 10, 100, 10, 5])
	print max_non_adjacent_sum_constant_space([1, 2, 3])
	print max_non_adjacent_sum_constant_space([1, 20, 3])

# test_max_non_adjacent_sum()