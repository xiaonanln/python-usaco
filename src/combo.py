"""
ID: isaiahl1
LANG: PYTHON2
TASK: combo
"""
TASK = 'combo'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	N = readint(fin)
	sol1 = readints(fin)
	sol2 = readints(fin)
	print 'sol', sol1, sol2
	count = 0
	for a in xrange(1,N+1):
		for b in xrange(1,N+1):
			for c in xrange(1,N+1):
				fit = dist(N, a, sol1[0]) <= 2 and dist(N, b, sol1[1]) <= 2 and dist(N, c, sol1[2]) <= 2
				if not fit:
					fit = dist(N, a, sol2[0]) <= 2 and dist(N, b, sol2[1]) <= 2 and dist(N, c, sol2[2]) <= 2
				if fit:
					# print 'fit', a, b, c
					count += 1

	print 'result', count
	print >>fout, count


def dist(N, a, b):
	if a > b:
		a, b = b, a
	# now b >= a
	return min(b-a, a+N-b)



def fit(n, digits):
	d = n % 10
	n //= 10
	if d not in digits:
		return False

	while n:
		d = n % 10
		n //= 10
		if d not in digits:
			return False

	return True

fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
