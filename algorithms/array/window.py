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

# print subarray_length_sum([2, 1, 4, 9, 2, 3, 8, 3, 4], 4)
# print subarray_length_sum([1, 2, 3, 2, 3, 4, 1], 4)
# print subarray_length_sum([4, 5, 7, 1, 2, 9, 8, 4, 3, 1], 4)

def subarray_max_sum_limited(l, k):
	curr_sum, max_sum = 0, 0
	start = 0
	for i in xrange(len(l)):
		if curr_sum > k:
			curr_sum -= l[start]
		else:
			curr_sum += l[i]
		if curr_sum > max_sum and curr_sum < k:
			max_sum = curr_sum
	return max_sum

print subarray_max_sum_limited([1, 2, 3, 4, 5], 11)
print subarray_max_sum_limited([2, 4, 6, 8, 10], 7)