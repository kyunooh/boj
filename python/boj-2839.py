n = int(input())
def bag(fives):
	if not fives:
	    fives = n // 5
	remainder = n // (fives * 5)
	if (remainder % 3) != 0:
		if fives == 0:
			return -1
		return bag(fives-1)
	else:
		return fives + (remainder // 3)

print(bag(None))