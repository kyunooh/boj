T = int(input())
N = []
def answer(a, n, c):
	if a < n:
		N.pop()
		return
	for i in range(1, 4, 1):
		N.append(i)
		if sum(N) == a:
			c += 1
		elif sum(N) > a:
			N.pop()
			continue
		else:
			n += 1
			c = answer(a, n, c)
		N.pop()
	return c

for _ in range(T):
	a = int(input())
	print(answer(a, 0, 0))

