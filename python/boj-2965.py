l = sorted(list(map(int, input().split())))


if l[1] - l[0] > l[2] - l[1]:
    print(l[1] - l[0] - 1)
else:
    print(l[2] - l[1] - 1)

