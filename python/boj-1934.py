T = int(input())

def get_max_div(a, b):
	max_div = 1	
	m = min(a, b)

	for i in range(m, 1, -1):
		if a % m == 0 and b % m == 0:
			max_div = i
			break
	return max_div


for _ in range(T):
	a, b = tuple(map(int, input().split()))
	max_div = get_max_div(a, b)

	print(max_div * max_div * a * b)


