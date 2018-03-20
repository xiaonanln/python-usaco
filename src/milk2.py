"""
ID: isaiahl1
LANG: PYTHON2
TASK: milk2
"""

import operator

fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

def main():
	"""
	3
	300 1000
	700 1200
	1500 2100
	:return:
	"""
	N = int(fin.readline())
	ranges = []
	for _ in xrange(N):
		a, b = map(int, fin.readline().strip().split())
		ranges.append( (a, b) )

	r1, r2 = solve(ranges)
	print >>fout, r1, r2

def solve(ranges):
	N = len(ranges)
	ranges.sort(key=operator.itemgetter(0)) # sort by start time

	# print 'ranges', ranges
	beginMilkTime, stopMilkTime = ranges[0]
	maxMilk = stopMilkTime - beginMilkTime
	maxGap = 0
	for i in xrange(1, N):
		a, b = ranges[i]
		if a <= stopMilkTime:
			if b > stopMilkTime:
				stopMilkTime = b
				maxMilk = max(maxMilk, stopMilkTime - beginMilkTime)
		else: # a > stopMilkTime
			gap = a - stopMilkTime
			maxGap = max(maxGap, gap)

			beginMilkTime, stopMilkTime = a, b

	return maxMilk, maxGap


with fin:
	with fout:
		main()
