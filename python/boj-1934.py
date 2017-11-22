T = int(input())

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

for _ in range(T):
    a, b = tuple(map(int, input().split()))
    max_div = gcd(a, b)
    
    print(max_div * (a // max_div) * (b // max_div))



