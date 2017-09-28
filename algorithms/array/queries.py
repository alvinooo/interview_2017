def index_after_range_reversals(a, ranges, index):
	for r in ranges:
		if r[0] <= index <= r[1]:
			index = r[0] + r[1] - index
	return a[index]

print index_after_range_reversals([10, 20, 30, 40, 50], [(1,4), (0,2)], 1)