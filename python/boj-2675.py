t = int(input())

for _ in range(t):
	r, s = input().split()
	r = int(r)
	final = ''
	for i in range(len(s)):
		final += (s[i] * r)
	print(final)