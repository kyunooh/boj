T = int(input())

for _ in range(T):
	h1, m1, a1, d1, h2, m2, a2, d2 = tuple(map(int, input().split()))
	h = h1 + h2
	m = m1 + m2
	a = a1 + a2
	d = d1 + d2
	if h < 1:
		h = 1
	if m < 1:
		m = 1
	if a < 0:
		a = 0

	t =  h + m * 5 + a * 2 + d * 2
	print(t)
