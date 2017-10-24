n = int(input())
a, b = 1, 7
difference = 6
count = 1

if n == 1:
    pass
else:
    while True:
        count += 1
        if n > a and n <= b:
            break
        a += difference
        difference += 6
        b += difference
print(count)
