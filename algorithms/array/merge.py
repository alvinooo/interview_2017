import heapq

def merge_k_arrays(*arrays):
	n = len(arrays[0])
	result = []
	heap = []
	curr_index = [1] * len(arrays)
	for i in xrange(len(arrays)):
		heapq.heappush(heap, (arrays[i][0], i))
	while heap:
		item, array_index = heapq.heappop(heap)
		result.append(item)
		curr_index[array_index] += 1
		if curr_index[array_index] < n:
			heapq.heappush(heap, (arrays[array_index][curr_index[array_index]], array_index))
	return result

def test_merge_k_arrays():
	print merge_k_arrays([1, 5, 8, 9],[2, 3, 7, 10],[4, 6, 11, 15],[9, 14, 16, 19],[2, 4, 6, 9])

# test_merge_k_arrays()