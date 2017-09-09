# 1 2 4 5 8 9 10
1
10
100
101
1000
1001
1010

import math

def nonadjacent_ones(n):
	for i in xrange(1, 2 ** n):
		if i & (i << 1) == 0:
			print i,
	print

print nonadjacent_ones(4)
print nonadjacent_ones(3)