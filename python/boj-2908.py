a, b = tuple(map(int, input().split()))

a_h = a // 100
a_t = a // 10 % 10
a_o = a % 10

a = a_o * 100 + a_t * 10 + a_h

b_h = b // 100
b_t = b // 10 % 10
b_o = b % 10

b = b_o * 100 + b_t * 10 + b_h

print(str(max(a,b)))
