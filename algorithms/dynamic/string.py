def edit_dist(s1, s2):
	edit_dist_table = [[0 for _ in s2] for _ in s1]
	for i in xrange(len(s1)):
		for j in xrange(len(s2)):
			if i == 0:
				edit_dist_table[i][j] = j
			elif j == 0:
				edit_dist_table[i][j] = i
			elif s1[i] == s2[j]:
				edit_dist_table[i][j] = edit_dist_table[i - 1][j - 1]
			else:
				edit_dist_table[i][j] = 1 + min(edit_dist_table[i - 1][j - 1],
					edit_dist_table[i][j - 1], edit_dist_table[i - 1][j])
	return edit_dist_table[i][j]

def test_edit_dist():
	print edit_dist("geek", "gesek")
	print edit_dist("cat", "cut")
	print edit_dist("sunday", "saturday")

# test_edit_dist()

def longest_common_substring(s1, s2):
	max_length, max_i, max_j = 0, 0, 0
	lengths = [[0 for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]
	for i in xrange(1, len(s1) + 1):
		for j in xrange(1, len(s2) + 1):
			if i == 0 or j == 0:
				lengths[i][j] = 0
			elif s1[i - 1] == s2[j - 1]:
				lengths[i][j] = 1 + lengths[i - 1][j - 1]
				if lengths[i][j] > max_length:
					max_length = lengths[i][j]
					max_i, max_j = i, j
			else:
				lengths[i][j] = 0
	return s1[i-max_length:i]

def test_longest_common_substring():
	print longest_common_substring("caba", "abac")
	print longest_common_substring("abacdfgdcaba", "abacdgfdcaba")

test_longest_common_substring()