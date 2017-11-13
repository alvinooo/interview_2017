def reverse_words(s):
	rev_list = [c for c in s]
	start, end = 0, len(s) - 1
	while start < end:
		rev_list[start], rev_list[end] = rev_list[end], rev_list[start]
		start += 1
		end -= 1
	start, end = 0, 0
	while end < len(rev_list):
		while end < len(rev_list) and rev_list[end] != ' ':
			end += 1
		tmp_start, tmp_end = start, end - 1
		while tmp_start < tmp_end:
			rev_list[tmp_start], rev_list[tmp_end] = rev_list[tmp_end], rev_list[tmp_start]
			tmp_start += 1
			tmp_end -= 1
		start = end + 1
		end = start
	return ''.join(rev_list)

def reverse_word_letters(s):
	rev_list = [c for c in s]
	start, end = 0, 0
	while end < len(rev_list):
		while end < len(rev_list) and rev_list[end] != ' ':
			end += 1
		tmp_start, tmp_end = start, end - 1
		while tmp_start < tmp_end:
			rev_list[tmp_start], rev_list[tmp_end] = rev_list[tmp_end], rev_list[tmp_start]
			tmp_start += 1
			tmp_end -= 1
		start = end + 1
		end = start
	return ''.join(rev_list)

def test_reverse_words():
	print reverse_words("the sky is blue")
	print reverse_words("Hi I am Cat")
	print reverse_word_letters("Let's take LeetCode contest")

# test_reverse_words()