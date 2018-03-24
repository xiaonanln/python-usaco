"""
ID: isaiahl1
LANG: PYTHON2
TASK: transform
"""
TASK = 'transform'

from itertools import izip

class Square(object):
	def __init__(self, N, lines):
		self.N = N
		self.grid = [
			list(line) for line in lines
		]
		self.grid2 = [
			[''] * N for _ in xrange(N)
		]

	def __str__(self):
		return '\n'.join( ''.join(row) for row in self.grid )

	def __eq__(self, other):
		return self.grid == other.grid

	def rotate1(self):
		N = self.N
		for r in xrange(N):
			for c in xrange(N):
				self.grid2[r][c] = self.grid[N-1-c][r]

		self.grid, self.grid2 = self.grid2, self.grid

	def rotate2(self):
		self.rotate1()
		self.rotate1()

	def rotate3(self):
		N = self.N
		for r in xrange(N):
			for c in xrange(N):
				self.grid2[r][c] = self.grid[c][N-1-r]

		self.grid, self.grid2 = self.grid2, self.grid

	def reflection(self):
		N = self.N
		for r in xrange(N):
			for c in xrange(N):
				self.grid2[r][c] = self.grid[r][N-1-c]

		self.grid, self.grid2 = self.grid2, self.grid

	def _combination(self):
		N = self.N
		for r in xrange(N):
			for c in xrange(N):
				self.grid2[r][c] = self.grid[N-1-r][c]

		self.grid, self.grid2 = self.grid2, self.grid

	def combination1(self):
		self._combination()
		self.rotate1()

	def combination2(self):
		self._combination()
		self.rotate2()

	def combination3(self):
		self._combination()
		self.rotate3()

def main(fin, fout):
	N = int(fin.readline())
	beginLines = [fin.readline().strip() for i in xrange(N)]
	targetLines = [fin.readline().strip() for i in xrange(N)]
	targetSquare = Square(N, targetLines)
	# print 'target\n', targetSquare, targetLines

	shortest = None
	for a in (0, 1, 2, 3):
		for b in (0, 1):
			for c in (0, 1, 2, 3, 4):
				square = Square(N, beginLines)
				if a == 1: square.rotate1()
				elif a == 2: square.rotate2()
				elif a == 3: square.rotate3()
				if b: square.reflection()
				if c == 1: square.combination1()
				elif c == 2: square.combination2()
				elif c == 3: square.combination3()
				elif c == 4: square._combination()
				# if a == 0 and b == 1 and c == 0:
				# 	print 'square\n', square
				# if a == 0 and b == 0 and c:
				# 	print 'c', c, 'square\n', square, 'target\n', targetSquare,square == targetSquare

				if square == targetSquare:
					transform = [x for x in (a, 4 if b else 0, 5 if c else 0) if x != 0]
					if not transform: transform = [6]
					print 'transform', transform
					if shortest is None or len(shortest) > len(transform) or (len(shortest) == len(transform) and shortest > transform):
						shortest = transform

	if shortest is None:
		sol = [7]
	else:
		sol = shortest

	print 'sol', sol

	print >>fout, ' '.join(map(str, sol))

fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
