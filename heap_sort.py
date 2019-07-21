def getChildren(i):
	return (2 * i + 1), (2 * i + 2)

def _heapify(data, n, i):
	largest = i
	l, r = getChildren(i)
	if l < n and data[i] < data[l]:
		largest = l
	if r < n and data[largest] < data[r]:
		largest = r
	if largest != i:
		data[i], data[largest] = data[largest], data[i]
		_heapify(data, n, largest)

def HeapSort(data):
	n = len(data)
	for i in range(n, -1, -1):
		_heapify(data, n, i)
	for i in range((n-1), 0, -1):
		data[i], data[0] = data[0], data[i]
		_heapify(data, i, 0)