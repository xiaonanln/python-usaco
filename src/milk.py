"""
ID: isaiahl1
LANG: PYTHON2
TASK: milk
"""
TASK = 'milk'

import operator

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def main(fin, fout):
	N, M = map(int, fin.readline().strip().split())
	print N, M
	farmers = []
	for i in xrange(M):
		farmers.append( readints(fin) )

	farmers.sort()
	print farmers
	cost = 0
	for price, units in farmers:
		buyUnits = min(units, N)
		cost += buyUnits * price
		N -= buyUnits
		if N == 0:
			break

	print >>fout, cost

fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
