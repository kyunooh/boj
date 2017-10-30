a, b, c, d, e = tuple(map(int, [input(), input(), input(), input(), input()]))

cheap = min(a + d, a + e, b + d, b + e, c + d, c + e)

print(cheap - 50)