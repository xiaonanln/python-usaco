"""
ID: isaiahl1
LANG: PYTHON2
TASK: wormhole
"""
TASK = 'wormhole'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	N = readint(fin)
	wormholes = []
	for _ in xrange(N):
		x, y = readints(fin)
		wormholes.append((x, y))

	print N, wormholes
	wormholeIndex = {wh: i for i, wh in enumerate(wormholes)}
	wormholesByY = {}
	for x,y in wormholes:
		wormholesByY.setdefault(y, []).append( (x, y) )
	graph = [[] for _ in xrange(N)]
	print 'wormholesByY', wormholesByY
	for y, wormholesY in wormholesByY.iteritems():
		wormholesY.sort()
		print y, wormholesY
		for i in xrange(0, len(wormholesY)-1):
			u = wormholeIndex[wormholesY[i]]
			v = wormholeIndex[wormholesY[i+1]]
			graph[u].append(v)

	connected = [False] * N
	connections = []

	def checkConnections():
		_connect = [-1] * N
		for u, v in connections:
			_connect[u] = v
			_connect[v] = u

		_graph  = [list(adj) for adj in graph] # copy the original graph
		for u, adj in enumerate(_graph):
			_graph[u] = [_connect[v] for v in adj]

		print 'connections', connections, 'new graph', _graph
		return checkLoop(_graph)

	def checkLoop(graph):
		visited = [False] * N
		for u in xrange(N):
			if not visited[u]:
				instack = [False] * N
				if dfs(graph, u, visited, instack):
					return True
		return False

	def dfs(graph, u, visited, instack):
		visited[u] = True
		instack[u] = True

		for v in graph[u]:
			print 'check', u, v, visited[v], instack[v]
			if not visited[v]:
				if dfs(graph, v, visited, instack): return True
			elif instack[v]: # found a loop
				return True

		instack[u] = False
		return False

	res = [0]
	def bt():
		if len(connections) == N //2:
			# all connected, calculate if there is a cycle in the directed graph
			print 'connections', connections
			if checkConnections():
				res[0] += 1

			return

		u = None
		for v, co in enumerate(connected):
			if not co:
				u = v
				break

		connected[u] = True

		for v in xrange(u+1, N):
			if not connected[v]:
				connected[v] = True

				# connect u -> v
				connections.append( (u, v) )

				bt()

				connected[v] = False
				connections.pop()

		connected[u] = False

	bt()
	print 'res', res[0]
	print >>fout, res[0]


fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
