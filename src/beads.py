"""
ID: isaiahl1
LANG: PYTHON2
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')


def main():
	with fin:
		with fout:
			N = int(fin.readline())
			S = fin.readline().strip()
			res = solve(N, S)
			# print 'res', res
			print >>fout, res

def solve(N, S):
	if not N:
		return 0

	S = list(S + S)
	# print S
	lastrb = (-1, 'w')
	for i, c in enumerate(S):
		if c == 'w': continue
		else: # c == 'r'/'b'
			if lastrb[1] == 'w' or lastrb[1] == c:
				for j in xrange(lastrb[0]+1, i):
					S[j] = c
			lastrb = (i, c)

	if lastrb[1] == 'w':
		return N

	for j in xrange(lastrb[0]+1, len(S)):
		S[j] = lastrb[1]

	# print S
	nums = []
	i = 0
	while i< 2*N:
		c1 = S[i]
		wl = 0
		while i<2*N and S[i] == c1:
			i += 1
			wl += 1
		nums.append(wl if c1 != 'w' else -wl)

	# print 'nums', nums
	if len(nums) == 1:
		return nums[0]//2
	maxcut = 0
	for i in xrange(1, len(nums)):
		# cut before i
		rl = nums[i]
		if rl < 0: continue # never cut before 'w'

		j = i+1
		while j < len(nums) and nums[j] < 0:
			rl += -nums[j]
			j += 1

		ll = 0
		j = i-1
		has_not_white = False
		while j >= 0:
			n_ = nums[j]
			if ll + abs(n_) + rl > N:
				break
			if n_ > 0:
				if has_not_white:
					break
				ll += n_
				has_not_white = True
			else:
				ll += -n_
			j -= 1

		# print i, nums[i-2:i+2], ll, rl, ll + rl
		maxcut = max(maxcut, ll+rl)

	return maxcut


















main()
