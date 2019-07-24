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

	def map(self, function):
		for item in self.data:
			function(item)

	def find(self, item):
		return item in self.data

	def __eq__(self, other):
		return self.data == other.data
