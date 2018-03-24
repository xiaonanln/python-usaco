"""
ID: isaiahl1
LANG: PYTHON2
TASK: barn1
"""
TASK = 'barn1'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	M, S, C = readints(fin)
	stalls = [readint(fin) for _ in xrange(C)]
	stalls.sort()
	print M, S, C, stalls
	gaps = [stalls[i] - stalls[i-1] - 1 for i in xrange(1, C)]
	gaps.sort(reverse=True)
	L = stalls[-1] - stalls[0] + 1
	print 'gaps', gaps, 'L', L
	for gap in gaps[:M-1]:
		L -= gap
	print 'result', L
	print >>fout, L


fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
