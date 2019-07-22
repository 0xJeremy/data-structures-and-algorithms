from collections import defaultdict

class Graph:
	def __init__(self, vertices=None):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def topologicalSortUtil(self, v, visited, stack):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		stack.insert(0, v)

	def topologicalSort(self):
		visited = [False] * self.V
		stack = []
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		return stack

	def DFSUtil(self, v, visited):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	def DFS(self, v):
		visited = [False] * (len(self.graph))
		self.DFSUtil(v, visited)

	def BFS(self, s):
		visited = [False] * (len(self.graph))
		queue = []
		queue.append(s)
		visited[s] = True
		while queue:
			s = queue.pop(0)
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True