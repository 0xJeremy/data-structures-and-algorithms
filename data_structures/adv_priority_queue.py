from heapq import heappush, heappop, heapify

class PriorityQueue():
	def __init__(self):
		self.data = []

	def parent(self, i):
		return (i-1)//2

	def insertKey(self, key):
		heappush(self.data, key)

	def decreaseKey(self, i, value):
		self.data[i] = value
		while i != 0 and self.data[self.parent(i)] > self.data[i]:
			self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]

	def extractMin(self):
		return heappop(self.data)

	def deleteKey(self, key):
		self.decreaseKey(key, float('-inf'))
		self.extractMin()

	def getMin(self):
		return self.data[0]
