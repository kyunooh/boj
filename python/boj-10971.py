import itertools

N = int(input())


W = []

for _ in range(N):
    W.append(list(map(int, input().split())))

min_w = 999999999999999
for p in itertools.permutations(range(N)):
    first = p[0]
    b = first
    w = 0
    for i in p[1:]:
        l = W[b][i]
        if l == 0:
            break
        w += l
        b = i
    if l == 0:
        break
    l = W[b][first]
    
    if l == 0:
        break
    w += l
    if w < min_w:
        min_w = w

print(min_w)

    
