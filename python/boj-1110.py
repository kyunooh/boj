n = int(input())
temp = n
count = 0
while True:
	t, o = (temp // 10), (temp % 10)
	s = t + o
	temp = (o * 10) + (s % 10)
	count += 1
	if temp == n:
		break
print(count)