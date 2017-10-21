n_list = list(range(1, 10000))
checks = [False] * 10000

def divided_sum(n):
	divided_sum = 0
	while n != 0:
		divided_sum += n % 10 
		n //= 10
	return divided_sum

def remove_on_list(n):
	if n >= 10000 or checks[n]:
		return

	i = n + (divided_sum(n))

	if i in n_list:
		n_list.remove(i)
	checks[n] = True
	remove_on_list(i)

for i in range(1, 10000):
	remove_on_list(i)

for n in n_list:
	print(n)
