import queue


def answer():
    count = 0
    n, d = tuple(map(int, input().split()))
    checks = [False] * 200001
    dist = [0] * 200001
    q = [n]
    checks[n] = True
    if d < n:
        return n - d 
    while len(q) != 0:
        n = q.pop(0)
        if n == d:
            return dist[n]
        minus = n - 1
        plus = n + 1
        double = n * 2
        if minus >= 0:
            if not checks[minus]:
                q.append(minus)
                checks[minus] = True
                dist[minus] = dist[n] + 1
        if plus <= 200000:
            if not checks[plus]:
                q.append(plus)
                checks[plus] = True
                dist[plus] = dist[n] + 1
        if double <= 200000:
            if not checks[double]:   
                q.append(double) 
                checks[double] = True
                dist[double] = dist[n] + 1
        

print(answer())