primes =[]

primes = list(range(1000,10000))

for i in range(2,10000):
	for j in primes.copy():
		if j < i:
			continue
		if j != i and j % i == 0:
			primes.remove(j)


def prime_checks(a, n, q, check, depth):
	if n in primes:
		if not check[n]:
			check[n] = True
			depth[n] = depth[a] + 1
			q.append(n)


T = int(input())


for _ in range(T):
	depth = [0] * 10000
	check = [False] * 10000 
	s, d =  tuple(map(int, input().split()))
	if s == d:
		print(0)
		continue
	q = []
	q.append(s)
	check[s] = True
	while len(q) != 0:
		a = q.pop(0)
		if check[d]:
			print(depth[d])
			break
		th = (a // 1000) * 1000
		h = (a // 100 % 10) * 100
		ten = (a % 100) // 10 * 10 
		o = a % 10
		for i in range(10):
			d_o = th + h + ten + i
			d_ten = th + h + o + i * 10 
			d_h = th + ten + o + i * 100
			d_th = h + ten + o + i * 1000
			for j in (d_o, d_ten, d_h, d_th):
				prime_checks(a, j, q, check, depth)
	if not check[d]: 
		print("impossible")

