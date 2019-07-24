def LIS(data):
	n = len(data)
	p = [0 for i in range(n)]
	m = [0 for i in range(n + 1)]
	L = 0
	for i in range(n):
		low = 1
		high = L
		while low <= high:
			mid = (low+high)//2
			if (data[m[mid]] < data[i]):
				low = mid+1
			else:
				high = mid-1

		newLow = low
		p[i] = m[newLow-1]
		m[newLow] = i

		if (newLow > L):
			L = newLow

	s = []
	k = m[L]
	for i in range(L-1, -1, -1):
		s.append(data[k])
		k = p[k]
	return s[::-1]
