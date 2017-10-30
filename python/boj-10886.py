t = int(input())

s = 0
for _ in range(t):
	s += int(input())

half = t / 2
if s > half:
	print('Junhee is cute!')
else:
	print('Junhee is not cute!')