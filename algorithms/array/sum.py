# https://leetcode.com/problems/two-sum/description/
def pair_sum(l, target):
	diff_to_index = {}
	for index, num in zip(xrange(len(l)), l):
		if num in diff_to_index:
			return sorted([index, diff_to_index[num]])
		diff_to_index[target - num] = index
	return None

def sorted_pair_sum(l, target):
	left, right = 0, len(l) - 1
	while left < right:
		curr_pair_sum = l[left] + l[right]
		if curr_pair_sum == target:
			return sorted([left + 1, right + 1])
		elif curr_pair_sum < target:
			left += 1
		else:
			right -= 1
	return None

def triple_sum(l, target):
	sorted_l = sorted(l)
	for fixed_index in xrange(len(l)):
		left, right = 0, len(l) - 1
		while left < right:
			curr_sum = l[left] + l[fixed_index] + l[right]
			if left == fixed_index:
				left += 1
			if right == fixed_index:
				right -= 1
			if curr_sum == target:
				return l[left], l[fixed_index], l[right]
			elif curr_sum < target:
				left += 1
			else:
				right -= 1
	return [None, None, None]

def test_sum():
	print pair_sum([2, 7, 11, 15], 9)
	print sorted_pair_sum([2, 7, 11, 15], 9)
	print triple_sum([12, 3, 4, 1, 6, 9], 24)
	print triple_sum([1, 4, 45, 6, 10, 8], 22)
test_sum()

# TODO
# https://www.programcreek.com/2014/07/leetcode-combination-sum-iv-java/
# https://www.programcreek.com/2013/02/leetcode-3sum-closest-java/
# https://leetcode.com/problems/3sum/description/