class Queue():
	def __init__(self):
		self.data = []

	def empty(self):
		self.data = []

	def size(self):
		return len(self.data)

	def back(self):
		return self.data[-1]

	def front(self):
		return self.data[0] if len(self.data) else None

	def pushBack(self, item):
		self.data.append(item)

	def popFront(self):
		return self.data.pop(0) if len(self.data) else None

	def __eq__(self, other):
		if len(self.data) != len(other.data):
			return False
		for i in range(len(self.data)):
			if self.data[i] != other.data[i]:
				return False
		return True