a, b, c = tuple(map(int, (input(), input(), input())))

mul = str(a * b * c)

for i in range(10):
	print(mul.count(str(i)))

