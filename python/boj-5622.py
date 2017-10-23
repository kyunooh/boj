k = input().upper()

d=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]


count = 0


for c in k:
    for i, s in enumerate(d,3):
        if c in s:
            count += i
            break
print(count)