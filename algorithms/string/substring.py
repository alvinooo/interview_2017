def longest_no_repeat_chars(s):
	max_length = 1
	start, end = 0, 0
	contains = set()
	while start < len(s) and end < len(s):
		if s[end] in contains:
			contains.remove(s[start])
			start += 1
		else:
			contains.add(s[end])
			end += 1
			max_length = max(max_length, end - start)
	return max_length

def longest_no_repeat_chars_optimized(s):
	max_length = 1
	start, end = 0, 0
	contains_at_index = {}
	for end in xrange(len(s)):
		if s[end] in contains_at_index:
			start = max(contains_at_index[s[end]], start)
		contains_at_index[s[end]] = end
		max_length = max(max_length, end - start)
	return max_length

def test_longest_no_repeat_chars():
	# print longest_no_repeat_chars("abcabcbb")
	print longest_no_repeat_chars_optimized("abcabcbb"), 3
	print longest_no_repeat_chars_optimized("bbbbb"), 1
	print longest_no_repeat_chars_optimized("pwwkew"), 3
	print longest_no_repeat_chars_optimized("abbcabc"), 3

test_longest_no_repeat_chars()