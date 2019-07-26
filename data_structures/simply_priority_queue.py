class PriorityQueue():
	def __init__(self):
		self.data = []

	def isEmpty(self):
		return len(self.queue) == []

	def size(self):
		return len(self.queue)

	def insert(self, data):
		self.data.append(data)

	def delete(self):
		if self.isEmpty():
			return None
		maxVal = 0
		for i in range(len(self.data)):
			if self.data[i] > self.data[maxVal]:
				maxVal = i
		item = self.data[maxVal]
		del self.data[maxVal]
		return item
