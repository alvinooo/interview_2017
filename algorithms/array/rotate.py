def count_rotate(array):
	# count = 0
	# for i in xrange(len(array) - 1):
	# 	if array[i] > array[i + 1]:
	# 		return count + 1
	# 	count += 1
	return 0

def test_count_rotate():
	print count_rotate([15, 18, 2, 3, 6, 12])
	print count_rotate([7, 9, 11, 12, 5])
	print count_rotate([7, 9, 11, 12, 15])

test_count_rotate()