def answer():
	S = set()
	count = 0
	n, d = tuple(map(int, input().split()))
	S = set()
	S.add(n)
	while True:
		if d in S:
			break
		new_S = set()
		for s in S:
			new_S.add(s - 1)
			new_S.add(s + 1)
			new_S.add(s * 2)
		S = new_S
		count += 1

	return count


print(answer())

# n이 ㅡ 
# S 에 N이 있는지 확인
# S 에 