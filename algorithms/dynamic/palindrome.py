def longest_subsequence(s):
	lengths = [[1 for _ in s] for _ in s]

	for length in xrange(1, len(s)):
		for start in xrange(len(s) - length):
			end = start + length
			if length <= 1:
				lengths[start][end] = length
			elif s[start] == s[end]:
				lengths[start][end] = 2 + lengths[start + 1][end - 1]
			else:
				lengths[start][end] = max(lengths[start - 1][end], lengths[start][end - 1])
	return lengths[0][len(s) - 1]

print longest_subsequence("BABCBAB")