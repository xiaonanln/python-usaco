"""
ID: isaiahl1
LANG: PYTHON2
TASK: dualpal
"""

def main(fin, fout):
	N, S = [int(x) for x in fin.read().strip().split()]

	while True:
		S += 1
		numPal = 0
		for base in (2,3,4,5,6,7,8,9,10):
			ss = strbase(S, base)
			if ss == ss[::-1]:
				numPal += 1
				if numPal == 2:
					break

		if numPal >= 2:
			print >>fout, S
			N -= 1
			if N == 0:
				break


DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def strbase(num, B):
	d = [DIGITS[num % B]]
	num //= B
	while num > 0:
		d.append(DIGITS[num % B])
		num //= B
	return ''.join(reversed(d))

TASK = 'dualpal'
fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
