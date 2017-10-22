l = list(map(int, (input(),input(),input(),input(),input())))
for i in range(len(l)):
	if l[i] < 40:
		l[i] = 40

print("%d" % (sum(l) / len(l)))