n = int(input())
l = list(filter(lambda x: x == n, map(int, input().split())))

print(len(l))

