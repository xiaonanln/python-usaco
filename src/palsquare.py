"""
ID: isaiahl1
LANG: PYTHON2
TASK: palsquare
"""

def main(fin, fout):
	B = int(fin.readline())
	res = solve( B )
	for a, b in res:
		print >>fout, a, b

def solve(B):
	res = []
	for N in xrange(1, 301):
		N2 = N*N
		N2 = fit(N2, B)
		if N2:
			res.append( (strbase(N, B), N2) )

	return res

def fit(num, B):
	s = strbase(num, B)
	return s if s == s[::-1] else None

DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def strbase(num, B):
	d = [DIGITS[num % B]]
	num //= B
	while num > 0:
		d.append(DIGITS[num%B])
		num //= B
	return ''.join(reversed(d))

TASK = 'palsquare'
fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
