for _ in range(3):
	yut = sum(map(int, input().split()))
	if yut == 4:
		print('E')
	elif yut == 3:
		print('A')
	elif yut == 2:
		print('B')
	elif yut == 1:
		print('C')
	else:
		print('D')