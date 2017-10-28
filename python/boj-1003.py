fibs = [0] * 41

fibs[0] = [1, 0]
fibs[1] = [0, 1]

for i in range(2, 41):
    fibs[i] = [fibs[i-2][0] + fibs[i-1][0], fibs[i-2][1] + fibs[i-1][1]]


t = int(input())

for _ in range(t):
    n = int(input())
    print(fibs[n][0], fibs[n][1])


 