n, k = tuple(map(int, input().split()))

l = [False] * (n + 1)


count = 0

answer = 0 
for i in range(2, n + 1):
	m = 1
	a = 0
	while a <= n + 1:
		a = i * m
		m += 1
		if a > n:
			break
		if not l[a]:
			l[a] = True
			count += 1
		if count == k:
			answer = a
			break
	if count == k:
		break

print(answer)
