word = input()
l = []
for i in range(ord('a'), ord('z') + 1):
	l.append(word.find(chr(i)))
print(' '.join(map(str, l)))