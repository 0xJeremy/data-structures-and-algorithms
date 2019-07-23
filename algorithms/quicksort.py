def partition(data, low, high):
	i = low - 1
	pivot = data[high]

	for j in range(low, high):
		if data[j] <= pivot:
			i += 1
			data[i], data[j] = data[j], data[i]
	data[i+1], data[high] = data[high], data[i+1]
	return i + 1

def _quickSort(data, low, high):
	if low < high:
		tmp = partition(data, low, high)
		_quickSort(data, low, tmp-1)
		_quickSort(data, tmp+1, high)

	return data

def QuickSort(data):
	return _quickSort(data, 0, len(data)-1)