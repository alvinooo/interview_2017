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

def test_longest_subsequence():
	print longest_subsequence("BABCBAB")

# test_longest_subsequence()

def rec_longest_substring(s):
	if len(s) <= 1:
		return s
	elif s[0] == s[-1]:
		mid = rec_longest_substring(s[1:-1])
		if len(mid) == len(s) - 2:
			return s
		else:
			return mid
	else:
		truncate_first = rec_longest_substring(s[1:])
		truncate_last = rec_longest_substring(s[:-1])
		truncate_both = rec_longest_substring(s[1:-1])
		return max(truncate_first,
			truncate_last,
			truncate_both,
			key=len)

# https://leetcode.com/articles/longest-palindromic-substring/
def longest_substring(s):
	max_start, max_end = len(s) - 1, 0
	lengths = [[0 for _ in s] for _ in s]
	lengths[0] = [1 for _ in s]
	lengths[1] = [1 for _ in s]
	for i in xrange(len(s) - 1):
		if s[i] == s[i + 1]:
			lengths[2][i] = 1
	for length in xrange(3, len(s)):
		for start in xrange(len(s) - length, -1, -1):
			end = start + length - 1
			curr_start, curr_end = len(s) - 1, 0
			if s[start] == s[end] and lengths[length - 2][start + 1]:
				lengths[length][start] = 1
				curr_start, curr_end = start, end
			else:
				lengths[length][start] = 0

			max_start, max_end = max((max_start, max_end), (curr_start, curr_end),
				key=lambda boundaries: boundaries[1] - boundaries[0])

	for length in lengths:
		print length
	print max_start, max_end
	return s[max_start:max_end+1]

def test_longest_substring():
	print rec_longest_substring("forgeeksskeegfor")
	print longest_substring("forgeeksskeegfor")

# test_longest_substring()