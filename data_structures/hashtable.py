class HashTable():
	def __init__(self):
		self.data = {}

	def insert(self, key, value):
		self.data[key] = value

	def remove(self, key):
		self.data[key] = None

	def find(self, key):
		return key in self.data

	def empty(self):
		self.data = {}

	def map(self, function):
		for key in self.data:
			function(key, self.data[key])

	def __eq__(self, other):
		return self.data == other.data
