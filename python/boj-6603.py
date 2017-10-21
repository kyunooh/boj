import itertools

while True:
	l = list(map(int, input().split()))
	if l[0] == 0:
		break
	for a in itertools.combinations(l[1:], 6):
		print(" ".join(map(str, a)))
	print()
