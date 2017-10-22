from sys import stdin

t = int(stdin.readline())

def next_permutation(permutation, n, answer=False):
	if answer:
		print(' '.join(map(str, permutation)))
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
	
	return True



def prev_permutation(permutation, n):
	i = n - 1;
	while i > 0 and permutation[i-1] <= permutation[i]:
		i -= 1
	if i <= 0:
		return False
	j = n - 1;
	while permutation[j] >= permutation[i-1]:
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
count = 1
permutation = first_permutation

k = stdin.readline()

if k[0] == "1":
	while True:
		number = list(map(int, k.split()))[1]
		answer = number == count	
		next_permutation(permutation, t, answer)
		if answer:
			break
		count += 1

else:
	while True:
		input_permutation = list(map(int, k.split()))[1:]
		next_permutation(permutation, t)
		count += 1
		if input_permutation == permutation:
			print(count)
			break

		
