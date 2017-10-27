import sys
n = int(input())

for _ in range(n):
	a, b = tuple(map(int, sys.stdin.readline().split()))
	i = a % 10
	count = 0
	temp = a
	while True:
		count += 1
		temp = temp * a
		if temp % 10 == i: 
			break
	j = b % count
	if j == 0:
		j = count
	answer = a ** j % 10
	if answer == 0:
		print(10)
	else:
		print(answer)