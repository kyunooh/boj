from sys import stdin

t = int(stdin.readline())
N = list(map(int, stdin.readline().split()))

def next_permutation(permutation, n):
	i = n - 1;
	while i > 0 and permutation[i-1] >= permutation[i]:
		i -= 1
	if i <= 0:
		return False
	j = n - 1;
	while permutation[j] <= permutation[i-1]:
		j -= 1
	permutation[i-1], permutation[j] = permutation[j], permutation[i-1]
	j = n - 1;
	while i < j:
		permutation[i], permutation[j] = permutation[j], permutation[i]
		i += 1
		j -= 1
	print(' '.join(map(str, permutation)))
	return True


first_permutation = list(range(1, t + 1))
count = 0
permutation = first_permutation
if not next_permutation(N, t):
	print(-1)
