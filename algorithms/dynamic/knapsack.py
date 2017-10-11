def greedy_change(v, coins):
	change = []
	greedy_coins = reversed(sorted(coins))
	remaining = v
	while remaining > 0:
		for coin in greedy_coins:
			while remaining >= coin:
				change.append(coin)
				remaining -= coin
	return change

# coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
# print greedy_change(200, coins)
# print greedy_change(70, coins)
# print greedy_change(121, coins)

def recursive_change(v, coins):
	if v == 0:
		return 0
	return 1 + min([recursive_change(v - coin, coins) for coin in coins if coin <= v])

# print recursive_change(30, [25, 10, 5]) # 2
# print recursive_change(11, [9, 6, 5, 1]) # 2

def dynamic_change(v, coins):
	min_change = [v for _ in xrange(v + 1)]
	min_change[0] = 0
	for value in xrange(1, v + 1):
		curr_min = v
		for coin in coins:
			if coin <= value and min_change[value - coin] < curr_min:
				curr_min = 1 + min_change[value - coin]
		min_change[value] = curr_min
	return min_change[-1]

print dynamic_change(30, [25, 10, 5]) # 2
print dynamic_change(11, [9, 6, 5, 1]) # 2