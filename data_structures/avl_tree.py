class Node:
	def __init__(self, data):
		self.data = data
		self.l = None
		self.r = None
		self.height = 1

class AVLTree():
	def __init__(self):
		self.root = None

	def insert(self, data):
		self.root = self._insert(self.root, data)

	def _insert(self, node, data):
		if not node:
			return Node(data)
		elif data < node.data:
			node.l = self._insert(node.l, data)
		else:
			node.r = self._insert(node.r, data)

		node.height = 1 + max(self._getHeight(node.l), self._getHeight(node.r))
		balance = self.getBalance(node)

		if balance > 1 and data < node.l.data:
			return self._rightRotate(node)
		if balance < -1 and data > node.r.data:
			return self._leftRotate(node)
		if balance > 1 and data > node.l.data:
			node.l = self._leftRotate(root.l)
			return self._rightRotate(node)
		if balance < -1 and data < node.r.data:
			node.r = self._rightRotate(node.r)
			return self._leftRotate(node)
		return node

	def delete(self, data):
		self.root = self._delete(self.root, data)

	def _delete(self, node, data):
		if not node:
			return node
		elif data < node.data:
			node.l = self._delete(node.l, data)
		elif data > node.data:
			node.r = self._delete(node.r, data)
		else:
			if node.l == None:
				tmp = node.r
				node = None
				return tmp
			elif node.r == None:
				tmp = node.l
				node = None
				return tmp
			tmp = self.getMinValue(node.r)
			node.data = tmp.data
			node.r = self._delete(node.r, tmp.data)

		if node == None:
			return node
		node.height = 1 + max(self._getHeight(node.l), self._getHeight(node.r))
		balance = self.getBalance(node)

		if balance > 1 and self.getBalance(node.l) >= 0:
			return self._rightRotate(node)
		if balance < -1 and self.getbalance(node.r) <= 0:
			return self._leftRotate(node)
		if balance > 1 and self.getbalance(node.l) < 0:
			node.l = self._leftRotate(node.l)
			return self._rightRotate(node)
		if balance < -1 and self.getBalance(node.r) > 0:
			node.r = self._rightRotate(node.r)
			return self._leftRotate(node)
		return node

	def _leftRotate(self, pivot):
		node = pivot.r
		tmp = node.l

		node.l = pivot
		pivot.r = tmp

		pivot.height = 1 + max(self._getHeight(pivot.r), self._getHeight(pivot.r))
		node.height = 1 + max(self._getHeight(node.l), self._getHeight(node.r))

		return node

	def _rightRotate(self, pivot):
		node = pivot.l
		tmp = node.r

		node.r = pivot
		pivot.l = tmp

		pivot.height = 1 + max(self._getHeight(pivot.l), self._getHeight(pivot.r))
		node.height = 1 + max(self._getHeight(node.l), self._getHeight(node.r))

		return node

	def _getHeight(self, node):
		if not node:
			return 0
		return node.height

	def getBalance(self, node):
		if not node:
			return 0
		return self._getHeight(node.l) - self._getHeight(node.r)

	def getMinValue(self, node):
		if node == None or node.l == None:
			return node
		return self.getMinValue(node.r)

	def preOrder(self):
		self._preOrder(self.root)

	def _preOrder(self, root): 
		if not root: 
			return
  
		print("{0} ".format(root.data), end="") 
		self._preOrder(root.l) 
		self._preOrder(root.r)
