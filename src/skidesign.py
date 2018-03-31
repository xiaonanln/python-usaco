"""
ID: isaiahl1
LANG: PYTHON2
TASK: skidesign
"""
TASK = 'skidesign'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	N = readint(fin)
	hills = []
	for _ in xrange(N):
		hills.append(readint(fin))

	print N, hills
	hills.sort()
	minHeight = min(hills)
	maxHeight = max(hills)
	print 'min', minHeight, 'max', maxHeight
	minimalCost = float('inf')
	for adjMinHeight in xrange(minHeight, maxHeight-17+1):
		print adjMinHeight, adjMinHeight+17
		raiseCost = 0
		for height in hills:
			if height >= adjMinHeight: break
			raiseCost += (adjMinHeight - height)**2

		lowerCost = 0
		for height in reversed(hills):
			if height <= adjMinHeight+17: break
			lowerCost += (height - adjMinHeight-17) ** 2

		totalCost = raiseCost + lowerCost
		minimalCost = min(minimalCost, totalCost)

	print >>fout, minimalCost


fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
