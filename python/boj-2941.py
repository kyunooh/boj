w = input()

count = 0
while len(w) != 0:
	if w[:3] == 'dz=':
		w = w[3:]
	elif w[:2] in ('c=', 'c-', 'd-', 'lj','nj', 's=', 'z='):
		w = w[2:]
	else:
		w = w[1:]
	count +=1

print(count)
