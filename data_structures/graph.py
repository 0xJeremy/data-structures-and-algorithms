class Graph():
	def __init__(self, vertices=None):
		self.vertex = vertices or {}

	def vertices(self):
		return list(self.vertex.keys())

	def edges(self):
		return self._generateEdges()

	def addVertex(self, vertex):
		if vertex not in self.vertex:
			self.vertex[vertex] = []

	def addEdge(self, edge):
		edge = set(edge)
		vertex1 = edge.pop()
		if edge:
			vertex2 = edge.pop()
		else:
			vertex2 = vertex1
		if vertex1 in self.vertex:
			self.vertex[vertex1].append(vertex2)
		else:
			self.vertex[vertex1] = [vertex2]

	def _generateEdges(self):
		edges = []
		for vertex in self.vertex:
			for neighbor in self.vertex[vertex]:
				if {neighbor, vertex} not in edges:
					edges.append({vertex, neighbor})

	def findIsolatedVertices(self):
		graph = self.vertex
		isolated = []
		for vertex in graph:
			if not graph[vertex]:
				isolated += [vertex]
		return isolated

	def findPath(self, start, end, path=[]):
		graph = self.vertex
		path = path + [start]
		if start == end:
			return path
		if start not in graph:
			return None
		for vertex in graph:
			if vertex not in graph:
				extended_path = self.findPath(vertex, end, path)
				if extended_path:
					return extended_path
		return None

	def findAllPaths(self, start, end, path=[]):
		graph = self.vertex
		path = path + [start]
		if start == end:
			return [path]
		if start not in graph:
			return []
		paths = []
		for vertex in graph[start]:
			if vertex not in path:
				extended_path = self.findAllPaths(vertex, end, path)
				for p in extended_path:
					paths.append(p)
		return paths
