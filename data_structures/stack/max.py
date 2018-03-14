# https://www.geeksforgeeks.org/find-maximum-sum-possible-equal-sum-three-stacks/
def max_equal_sum(s1, s2, s3):
	i1, i2, i3 = map(len, [s1[:-1], s2[:-1], s3[:-1]])
	sum1, sum2, sum3 = map(sum, [s1, s2, s3])
	while not (sum1 == sum2 == sum3):
		if sum1 >= sum2 and sum1 >= sum3:
			sum1 -= s1[i1]
			i1 -= 1
		elif sum2 >= sum1 and sum2 >= sum3:
			sum2 -= s2[i2]
			i2 -= 1
		elif sum3 >= sum1 and sum3 >= sum2:
			sum3 -= s3[i3]
			i3 -= 1
	return sum1

# print max_equal_sum([3, 10], [4, 5], [2, 1])
# print max_equal_sum([1, 1, 1, 2, 3], [2, 3, 4], [1, 4, 5, 2])

# https://www.geeksforgeeks.org/next-greater-element/
def next_greater_element(l):
	s = []
	for i in l:
		while s and i > s[-1]:
			print "{} -> {}".format(s[-1], i)
			s.pop()
		s.append(i)
	while s:
		print "{} -> -1".format(s[-1])
		s.pop()

def test_next_greater_element():
	next_greater_element([4,5,2,25])

# test_next_greater_element()
