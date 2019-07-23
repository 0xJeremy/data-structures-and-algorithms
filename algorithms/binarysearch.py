def _binarySearch(data, l, r, x):
	if r >= l:
		mid = int(l + (r - l)/2)
		if data[mid] == x:
			return mid
		elif data[mid] > x:
			return _binarySearch(data, l, mid-1, x)
		else:
			return _binarySearch(data, mid+1, r, x)

def BinarySearch(data, val):
	return _binarySearch(data, 0, len(data)-1, val)