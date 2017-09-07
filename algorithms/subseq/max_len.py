def contiguous(seq):
	max_lens = [1 for _ in seq]
	for i in xrange(len(seq)):
		for j in xrange(i):
			if abs(seq[i] - seq[j]) <= 1 and max_lens[i] <= max_lens[j]:
				max_lens[i] = max_lens[j] + 1
	return max(max_lens)

print contiguous([2, 5, 6, 3, 7, 6, 5, 8])
print contiguous([-2, -1, 5, -1, 4, 0, 3])