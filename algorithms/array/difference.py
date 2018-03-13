def max_diff_larger_before_smaller(l):
	curr_min, max_diff = l[0], l[1] - l[0]
	for i in xrange(1, len(l)):
		max_diff = max(max_diff, l[i] - curr_min)
		curr_min = min(curr_min, l[i])
	return max_diff

def test_max_diff_larger_before_smaller():
	print max_diff_larger_before_smaller([2, 3, 10, 6, 4, 8, 1])
	print max_diff_larger_before_smaller([7, 9, 5, 6, 3, 2])

# test_max_diff_larger_before_smaller()

def buy_sell_stock(prices):
	local_mins = []
	local_maxs = []

	index = 0
	while index < len(prices) - 1:
		while index < len(prices) - 1 and prices[index] > prices[index + 1]:
			index += 1
		local_mins.append(index)
		while index < len(prices) - 1 and prices[index] < prices[index + 1]:
			index += 1
		local_maxs.append(index)
	return zip(local_mins, local_maxs)

print buy_sell_stock([100, 180, 260, 310, 40, 535, 695])
print buy_sell_stock(xrange(10, 1, -1))