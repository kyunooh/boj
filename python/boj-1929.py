m, n = tuple(map(int, input().split()))

l = [True] * (n + 2)
if n >= 0:
	l[0] = False
	l[1] = False
for i in range(2, n + 1):
	j = 2
	while True:
		a = i * j
		if a > n:
			break
		l[a] = False
		j += 1


n_l = list(range(2, n + 1))
l = list(filter(lambda x: x >= m and l[x], n_l))
for i in l:
	print(i)
