def subarray_length_sum(l, k):
	sum_length = 0
	curr_len = 0
	max_encountered = False
	for elem in l:
		if elem <= k:
			curr_len += 1
			max_encountered = elem == k
		else:
			if max_encountered:
				sum_length += curr_len
			max_encountered, curr_len = False, 0
	return sum_length + curr_len

print subarray_length_sum([2, 1, 4, 9, 2, 3, 8, 3, 4], 4)
print subarray_length_sum([1, 2, 3, 2, 3, 4, 1], 4)
print subarray_length_sum([4, 5, 7, 1, 2, 9, 8, 4, 3, 1], 4)