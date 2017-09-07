def count_sum_pairs(l, total):
	count = 0
	num_map = {}
	for num in l:
		if num not in num_map:
			num_map[num] = 0
		num_map[num] += 1
	for num in l:
		if total - num in num_map:
			count += num_map[total - num]
		if num == total - num:
			count -= 1
	return count / 2

print count_sum_pairs([1,5,7,-1], 6)
print count_sum_pairs([1,5,7,-1,5], 6)
print count_sum_pairs([1,1,1,1], 2)
print count_sum_pairs([10,12,10,15,-1,7,6,5,4,2,1,1,1], 11)

def count_sum_triplets(l, total):
	count = 0