x = int(input())

def get_count(x):
	if x < 100:
		return x
	count = 99
	for i in range(100, x + 1):
		a, b, c = i // 100, i // 10 % 10, i % 10
		if a - b == b - c:
			count += 1
	return count


print(get_count(x))
