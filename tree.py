# REMOVE FUNCTION CURRENTLY DOES NOT WORK IN ALL CASES

class Node():
	def __init__(self, data=None):
		self.data = data
		self.l = None
		self.r = None

	def __eq__(self, other):
		if not other: return False
		return self.data == other.data
	def __ne__(self, other):
		if not other: return True
		return self.data != other.data
	def __lt__(self, other):
		return self.data < other.data
	def __gt__(self, other):
		return self.data > other.data
	def __le__(self, other):
		return self.data <= other.data
	def __ge__(self, other):
		return self.data >= other.data


class BinaryTree():
	def __init__(self):
		self.head = Node()

	def insert(self, data):
		if self.head.data == None:
			self.head.data = data
		else:
			self._insert(self.head, Node(data))

	def _insert(self, node, data):
		if not node.l and data < node:
			node.l = data
		elif not node.r and data >= node:
			node.r = data
		elif data < node:
			self._insert(node.l, data)
		elif data >= node:
			self._insert(node.r, data)

	def remove(self, data):
		if self.head == None:
			return
		self._remove(self.head, Node(data))

	def _remove(self, node, data):
		if not node:
			return node
		if data < node:
			node.l = self._remove(node.l, data)
		elif data > node:
			node.r = self._remove(node.r, data)
		else:
			if not node.r:
				return node.l
			elif not node.l:
				return node.r
			tmp = self._getLeftmost(node.r)
			node = tmp
			node.r = self._remove(node.r, tmp)
		return node

	def _getLeftmost(self, node):
		curr = node
		while curr.l:
			curr = curr.l
		return curr

	def _inOrderMap(self, node, function):
		if node != None:
			self._inOrderMap(node.l, function)
			function(node)
			self._inOrderMap(node.r, function)

	def _preOrderMap(self, node, function):
		if node != None:
			function(node)
			self._preOrderMap(node.l, function)
			self._preOrderMap(node.r, function)

	def _postOrderMap(self, node, function):
		if node != None:
			self._postOrderMap(node.l, function)
			self._postOrderMap(node.r, function)
			function(node)

	@staticmethod
	def inOrderMap(tree, function):
		tree._inOrderMap(tree.head, function)

	@staticmethod
	def preOrderMap(tree, function):
		tree._preOrderMap(tree.head, function)

	@staticmethod
	def postOrderMap(tree, function):
		tree._postOrderMap(tree.head, function)