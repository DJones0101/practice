
graph = {
			
			'a':set(['b','s']),
			'b':set(['a']),
			'd':set(['c']),
			's':set(['c','g']),
			'c':set(['s','d','e','f']),
			'g':set(['s','f','h']),
			'e':set(['c','h']),
			'h':set(['g','e']),
			'f':set(['c','g'])
		}


graph1 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


graph2 = [
			[0,1,1,0,0,0],
			[1,0,0,1,1,0],
			[1,0,0,0,0,1],
			[0,1,0,0,0,0],
			[0,0,0,0,1,1],
			[0,0,1,0,1,0],
		]


def dfs(graph, start):

	stack = [start]
	visited = set()

	while stack:

		vertex = stack.pop()

		if vertex not in visited:

			visited.add(vertex)
			
			stack.extend(graph[vertex] - visited)

	return visited

def _dfs(graph, start):

	stack = [(start,start)]
	visited = []

	while stack:
		row, _= stack.pop()
		for col in range(len(graph[row])):
			value = graph[row][col]
			index = (row, col)
			print(value, index)
			if value == 1 and index not in visited:
				visited.append(index)
				stack.append(row)
	return visited


def bfs(graph, start):

	queue = [start]
	visited = set()

	while queue:

		vertex = queue.pop(0)

		if vertex not in visited:
			
			visited.add(vertex)
			
			queue.extend(graph[vertex] - visited)

	return visited




def short_bfs(graph, start, goal):

	queue = [(start, [start])]

	while queue:

		(vertex, path) = queue.pop(0)

		for next in graph[vertex] - set(path):

			if next == goal:

				yield  path + [next]

			else:
				queue.append((next,path + [next]))


def shortest(graph, start, goal):

	try:
		return next(short_bfs(graph, start, goal))
	except StopIteration:
		return None


print(_dfs(graph2, 0))