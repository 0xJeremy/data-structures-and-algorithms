def CountingSort(data, exp):
	n = len(data)
	output = [0 for i in range(n)]
	count = [0 for i in range(10)]

	for i in range(0, n):
		index = data[i]/exp
		count[int(index) % 10] += 1
	for i in range(1, 10):
		count[i] += count[i-1]
		
	i = n - 1
	while i >= 0:
		index = data[i] / exp
		output[count[int(index) % 10] - 1] = data[i]
		count[int(index) % 10] -= 1
		i -= 1

	return output

def RadixSort(data):
	m = max(data)

	exp = 1
	while m / exp > 0:
		data = CountingSort(data, exp)
		exp *= 10
	return data