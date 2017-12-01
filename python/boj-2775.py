T = int(input())
l = [list(range(1,15))]
for i in range(1, 14):
    l.append(([1]*14))
    for j in range(1, 14):
        l[i][j] = l[i][j-1] + l[i-1][j]




for _ in range(T):
    k, n = tuple(map(int, [input(), input()]))
    print(l[k][n-1])



# 1  5 14
# 1  4 10 20 31
# 1  3  6 10 15
# 1  2  3  4  5  6  7  8  9  10 11 12 13 14