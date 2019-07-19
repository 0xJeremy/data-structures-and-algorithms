class _Heap():
	def __init__(self):
		self.data = []

	def _get(self):
		return self.data[0] if len(self.data) else None

	def _extract(self):
		if self.size() == 0:
			return None
		elif self.size() == 1:
			return self.data.pop()
		tmp = self.data[0]
		self.data[0] = self.data.pop()
		self._heapifyDown(0)
		return tmp

	def size(self):
		return len(self.data)

	def insert(self, item):
		self.data.append(item)
		self._heapifyUp(self.size() - 1)

	@staticmethod
	def getParent(index):
		return int(index / 2)

	@staticmethod
	def getChildren(index):
		return index * 2, index * 2 + 1

class MinHeap(_Heap):
	def __init__(self):
		super().__init__()

	def getMin(self):
		return self._get()

	def extractMin(self):
		return self._extract()

	def _heapifyUp(self, index):
		if not index: return
		parent = self.getParent(index)
		if self.data[index] < self.data[parent]:
			tmp = self.data[parent]
			self.data[parent] = self.data[index]
			self.data[index] = tmp
			self._heapifyUp(parent)

	def _heapifyDown(self, index):
		child1, child2 = self.getChildren(index)
		if child2 > self.size() - 1: return
		minChild = index
		if self.data[child1] < self.data[minChild]:
			minChild = child1
		if self.data[child2] < self.data[minChild]:
			minChild = child2
		if minChild != index:
			tmp = self.data[index]
			self.data[index] = self.data[minChild]
			self.data[minChild] = tmp
			self._heapifyDown(minChild)

class MaxHeap(_Heap):
	def __init__(self):
		super().__init__()

	def getMax(self):
		return self._get()

	def extractMax(self):
		return self._extract()

	def _heapifyUp(self, index):
		if not index: return
		parent = self.getParent(index)
		if self.data[index] > self.data[parent]:
			tmp = self.data[parent]
			self.data[parent] = self.data[index]
			self.data[index] = tmp
			self._heapifyUp(parent)

	def _heapifyDown(self, index):
		child1, child2 = self.getChildren(index)
		if child2 > self.size() - 1: return
		minChild = index
		if self.data[child1] > self.data[minChild]:
			minChild = child1
		if self.data[child2] > self.data[minChild]:
			minChild = child2
		if minChild != index:
			tmp = self.data[index]
			self.data[index] = self.data[minChild]
			self.data[minChild] = tmp
			self._heapifyDown(minChild)
