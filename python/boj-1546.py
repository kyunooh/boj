N = input()
l = list(map(int, input().split()))

M = max(l)
l = list(map(lambda x: x / M * 100, l))

print("%.2f" % round(sum(l) / len(l), 2))