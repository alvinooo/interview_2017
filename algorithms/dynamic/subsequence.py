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

def rec_longest_common(s1, s2):
	if len(s1) == 0 or len(s2) == 0:
		return []
	elif s1[-1] == s2[-1]:
		return rec_longest_common(s1[:-1], s2[:-1]) + [s1[-1]]
	else:
		return max(
			rec_longest_common(s1[:-1], s2),
			rec_longest_common(s1, s2[:-1]),
			key=len)

def longest_common(s1, s2):
	lengths = [[0 for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]
	for i in xrange(1, len(s1) + 1):
		for j in xrange(1, len(s2) + 1):
			if s1[i - 1] == s2[j - 1]:
				lengths[i][j] = 1 + lengths[i - 1][j - 1]
			else:
				lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
	subsequence = []
	i = len(s1)
	j = len(s2)
	while i > 0 and j > 0:
		if s1[i - 1] == s2[j - 1]:
			subsequence.append(s1[i - 1])
			i -= 1
			j -= 1
		elif lengths[i - 1][j] > lengths[i][j - 1]:
			i -= 1
		else:
			j -= 1
	# for row in lengths:
	# 	print row
	return subsequence[::-1]

def test_rec_longest_common():
	print rec_longest_common([1,2,3,4,1],[3,4,1,2,1,3])
	print longest_common([1,2,3,4,1],[3,4,1,2,1,3])
	print rec_longest_common("ABCDGH","AEDFHR")
	print longest_common("ABCDGH","AEDFHR")
	print rec_longest_common("AGGTAB","GXTXAYB")
	print longest_common("AGGTAB","GXTXAYB")

# test_rec_longest_common()

def max_sum_k_dist(l, k):
	prev_max_ptr, prev_max_sum = 0, l[0]
	sums = l[:]
	for i in xrange(k + 1, len(l)):
		prev_max_sum = max(prev_max_sum, sums[prev_max_ptr])
		sums[i] = max(l[i] + prev_max_sum, sums[i - 1])
		prev_max_ptr += 1
	return sums[-1]

def test_max_sum_k_dist():
	print max_sum_k_dist([4, 5, 8, 7, 5, 4, 3, 4, 6, 5], 3)
	print max_sum_k_dist([50, 70, 40, 50, 90, 70, 60, 40, 70, 50], 2)

# test_max_sum_k_dist()