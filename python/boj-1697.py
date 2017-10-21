def answer():
    count = 0
    n, d = tuple(map(int, input().split()))
    S = set()
    S.add(n)
    if d < n:
        return n - d 
    while True:
        if d in S:
            break
        new_S = set()
        for s in S:
            if (s - 1) >= 0:
                new_S.add(s - 1)
                new_S.add(s + 1)
                new_S.add(s * 2)
        S = new_S
        count += 1
        gc.collect()

    return count

print(answer())