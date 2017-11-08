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

# test_nearest_element()

def almost_sorted(element, l):
	low, hi = 0, len(l) - 1
	while low <= hi:
		mid = low + (hi - low) / 2
		if l[mid] == element:
			return mid
		elif mid > low and l[mid - 1] == element:
			return mid - 1
		elif mid < hi and l[mid + 1] == element:
			return mid + 1
		elif l[mid] < element:
			low = mid + 2
		else:
			hi = mid - 2
	return -1

def test_almost_sorted():
	print almost_sorted(40, [10, 3, 40, 20, 50, 80, 70])
	print almost_sorted(90, [10, 3, 40, 20, 50, 80, 70])

# test_almost_sorted()