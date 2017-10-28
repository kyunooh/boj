l = [True] * 1001
l[0] = False
l[1] = False
for i in range(2, 1001):
	j = 2
	while True:
		a = i * j
		if a > 1000:
			break
		l[a] = False
		j += 1

input()


n = list(map(int, input().split()))
count = 0
for i in n:
	if l[i]:
		count += 1

print(count)
