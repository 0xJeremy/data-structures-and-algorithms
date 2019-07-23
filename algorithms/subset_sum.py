def _subsetSum(data, n, num):
	if num == 0:
		return True
	if n == 0 and num != 0:
		return False
	if (data[n - 1] > num):
		return _subsetSum(data, n - 1, num)
	return _subsetSum(data, n-1, num) or _subsetSum(data, n-1, num-data[n-1])

def SubsetSum(data, num):
	return _subsetSum(data, len(data), num)