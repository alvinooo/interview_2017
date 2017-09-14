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

print edit_dist("geek", "gesek")
print edit_dist("cat", "cut")
print edit_dist("sunday", "saturday")