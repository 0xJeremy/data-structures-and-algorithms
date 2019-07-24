class Stack():
	def __init__(self):
		self.data = []

	def empty(self):
		self.data = []

	def size(self):
		return len(self.data)

	def front(self):
		return self.data[0] if len(self.data) else None

	def back(self):
		return self.data[-1] if len(self.data) else None

	def push_back(self, item):
		self.append(item)

	def pop_back(self):
		return self.data.pop(0) if len(self.data) else None

	def map(self, function):
		for item in self.data:
			function(item)

	def find(self, item):
		return item in self.data

	def __eq__(self, other):
		return self.data == other.data
