"""
ID: isaiahl1
LANG: PYTHON2
TASK: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

def checkLeapYear(year):
	if year % 400 == 0: return True
	if year % 100 == 0: return False
	return year % 4 == 0

def getMonthDays(isLeapYear, month):
	if month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	elif month != 2:
		return 30
	else:
		return 29 if isLeapYear else 28

def solve():
	N = int(fin.read())
	weekday = 14;
	weekdayHits = [0, 0, 0, 0, 0, 0, 0]
	for year in xrange(1900, 1900+N):
		isLeapYear = checkLeapYear(year)
		for month in (1,2,3,4,5,6,7,8,9,10,11,12):

			weekdayHits[weekday % 7] += 1
			monthDays = getMonthDays( isLeapYear, month )
			weekday += monthDays

	print >>fout, ' '.join(map(str, weekdayHits))

with fin:
	with fout:
		solve()

