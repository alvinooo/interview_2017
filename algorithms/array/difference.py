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