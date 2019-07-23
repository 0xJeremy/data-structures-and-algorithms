def MergeSort(data):
	if len(data) > 1:
		mid = len(data) // 2
		l, r = data[:mid], data[mid:]
		MergeSort(l)
		MergeSort(r)

		i, j, k = 0, 0, 0

		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				data[k] = l[i]
				i += 1
			else:
				data[k] = r[j]
				j += 1
			k += 1

		while i < len(l):
			data[k] = l[i]
			i += 1
			k += 1
		while j < len(r):
			data[k] = r[j]
			j += 1
			k += 1