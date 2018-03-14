from collections import deque

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
			start += 1
		else:
			curr_sum += l[i]
		if curr_sum > max_sum and curr_sum < k:
			max_sum = curr_sum
	return max_sum

# print subarray_max_sum_limited([1, 2, 3, 4, 5], 11)
# print subarray_max_sum_limited([2, 4, 6, 8, 10], 7)

# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# https://www.youtube.com/watch?v=ShbRCjvB_yQ
# [1, 2, 3, 1, 4, 5, 2, 3, 6]

# [3, 3, 4, 5, 5, 5, 6]
# curr_max = 3, 4, 5
# 5, 2, 3

# k = 2
# [2, 3,]

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

def sliding_window_maximum(l, k):
	solution = []
	q = deque()
	for i in xrange(k):
		while q and l[q[-1]] <= l[i]:
			q.pop()
		q.append(i)
	for i in xrange(k, len(l)):
		solution.append(l[q[0]])
		while q and q[0] <= i - k:
			q.popleft()
		while q and l[q[-1]] <= l[i]:
			q.pop()
		q.append(i)
	solution.append(l[q[0]])
	return solution

def test_sliding_window_maximum():
	print sliding_window_maximum([12, 1, 78, 90, 57, 89, 56], 3)
	print sliding_window_maximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
	print sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)

test_sliding_window_maximum()