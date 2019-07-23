def _lcs(x, y, m, n):
	if m == 0 or n == 0:
		return 0
	elif x[m-1] == y[n-1]:
		return 1 + _lcs(x, y, m-1, n-1)
	else:
		return max(_lcs(x, y, m, n-1), _lcs(x, y, m-1, n))

def LCS(x, y):
	return _lcs(x, y, len(x), len(y))