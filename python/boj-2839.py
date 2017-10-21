
def answer():
	n = int(input())
	fives = n // 5
	return bag(n, fives)

def bag(n, fives):
	if fives != 0:
		remainder = n % (fives * 5)
	else:
		remainder = n
	if (remainder % 3) != 0:
		if fives == 0:
			return -1
		return bag(n, fives-1)
	else:
		return fives + (remainder // 3)

print(answer())