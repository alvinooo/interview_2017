def nearest_element(element, l):
	low, hi = 0, len(l) - 1
	while low <= hi:
		mid = low + (hi - low) / 2
		if element < l[mid]:
			hi = mid - 1
		elif element > l[mid]:
			low = mid + 1
		else:
			return l[mid]
	if abs(l[low] - element) < abs(l[hi] - element):
		return l[low]
	else:
		return l[hi]

def test_nearest_element():
	print nearest_element(36, [12, 16, 22, 30, 39, 42, 45, 48, 50, 53, 55, 56])

test_nearest_element()