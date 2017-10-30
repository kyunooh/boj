l = [''] * 5

for i in range(5):
	l[i] = input()

s = ''
for i in range(16):
	for j in range(5):
		if i >= len(l[j]):
			continue
		s += l[j][i] 

print(s)

