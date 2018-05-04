"""
ID: isaiahl1
LANG: PYTHON2
TASK: ariprog
"""
TASK = 'ariprog'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	N = readint(fin)
	M = readint(fin)
	squares = [i*i for i in xrange(0, 16)]
	bisquares = sorted(list(set([v1 + v2 for v1 in squares for v2 in squares])))
	print N, M, squares, 'bisquares', bisquares


fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
