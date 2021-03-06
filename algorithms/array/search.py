def common_elements(l1, l2, l3):
	p1, p2, p3 = 0, 0, 0
	while p1 < len(l1) and p2 < len(l2) and p3 < len(l3):
		if l1[p1] == l2[p2] == l3[p3]:
			print l1[p1],
		if l1[p1] < l2[p2]:
			p1 += 1
		elif l2[p2] < l3[p3]:
			p2 += 1
		else:
			p3 += 1

def test_common_elements():
	l1 = [1, 5, 5]
	l2 = [3, 4, 5, 5, 10]
	l3 = [5, 5, 10, 20]
	common_elements(l1, l2, l3)

	print

	l1 = [1, 5, 10, 20, 40, 80]
	l2 = [6, 7, 20, 80, 100]
	l3 = [3, 4, 15, 20, 30, 70, 80, 120]
	common_elements(l1, l2, l3)

# test_common_elements()

def closest_pair_sum(element, l1, l2):
	min_diff = element * len(l1) * len(l2)
	min_pair = (l1[0], l2[0])
	p1, p2 = 0, len(l2) - 1
	while p1 < len(l1) and p2 >= 0:
		curr_diff = abs(l1[p1] + l2[p2] - element)
		if curr_diff < min_diff:
			min_diff = curr_diff
			min_pair = (l1[p1], l2[p2])
		if l1[p1] + l2[p2] < element:
			p1 += 1
		else:
			p2 -= 1
	return min_pair

def test_closest_pair_sum():
	print closest_pair_sum(32, [1, 4, 5, 7], [10, 20, 30, 40])
	print closest_pair_sum(50, [1, 4, 5, 7], [10, 20, 30, 40])

# test_closest_pair_sum()