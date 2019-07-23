def SelectionSort(data):
	for i in range(len(data)):
		minIndex = i
		for j in range(i+1, len(data)):
			if data[minIndex] > data[j]:
				minIndex = j
		data[i], data[minIndex] = data[minIndex], data[i]
	return data