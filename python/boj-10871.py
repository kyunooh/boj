a, b = tuple(map(int, input().split()))

l = list(map(int, input().split()))

print(' '.join(list(map(str, (filter(lambda x: x < b, l)))))