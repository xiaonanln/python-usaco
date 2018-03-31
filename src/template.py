"""
ID: isaiahl1
LANG: PYTHON2
TASK: test
"""
TASK = 'test'

def readints(fin):
	return tuple(int(x) for x in fin.readline().split())

def readint(fin):
	return int(fin.readline())

def main(fin, fout):
	pass

fin = open (TASK + '.in', 'r')
fout = open (TASK + '.out', 'w')
with fin:
	with fout:
		main(fin, fout)
