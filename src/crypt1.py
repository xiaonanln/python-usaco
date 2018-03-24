"""
ID: isaiahl1
LANG: PYTHON2
TASK: crypt1
"""
TASK = 'crypt1'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	N = readint(fin)
	digits = readints(fin)

	count = 0
	print 'digits', digits
	for a in digits:
		if a == 0: continue
		for b in digits:
			for c in digits:
				for d in digits:
					if d == 0: continue
					for e in digits:
						# abc * de
						x = (a*100+b*10+c) * e
						y = (a*100+b*10+c) * d
						if x >= 1000 or y >= 1000: continue
						if not fit(x, digits) or not fit(y, digits): continue
						s = y*10 + x
						if fit(s, digits):
							print a,b,c,d,e, x, y, s
							count += 1

	print 'result', count
	print >>fout, count


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
