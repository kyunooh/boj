n = int(input())

def alphabets():
	return list(map(chr, range(ord('a'), ord('z') + 1)))

count = 0
for _ in range(n):
	w = input().lower()
	b = [False] * 26
	a = alphabets()
	is_continue = True

	for i in range(len(w)):
		index = ord(w[i]) - ord('a')
		if b[index]:
			if i > 0 and w[i-1] != w[i]: 
				is_continue = False
		else:
			b[index] = True


	if is_continue:
		count += 1

print(str(count))
