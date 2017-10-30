total = int(input())

remainder = 0
for _ in range(9):
	remainder += int(input())

print(total - remainder)