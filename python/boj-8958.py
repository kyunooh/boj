t = int(input())


for _ in range(t):
	ox_list = input()
	score = 0
	before_score = 0
	for i in range(len(ox_list)):
		if ox_list[i] == 'O':
			before_score += 1
			score += before_score
		else:
			before_score = 0
	print(score)