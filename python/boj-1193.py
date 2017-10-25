x = int(input())
a, b = 1, 1
count = 0
answer = ""
m = 1
r = False
while True:
	count += 1
	if x == count:
		answer = str(a) + "/" + str(b)
		break

	if b == m and a % 2 == 1 and not r:
		m += 1
		a = 1
		b = m
		r = True
	elif a == m and a % 2 == 0:
		m += 1
		b = 1
		a = m
		r = False
	elif r:
		b -= 1
		a += 1
	else:
		b += 1
		a -= 1


print(answer)