T = int(input())


def get_room(h, w, n):
    for i in range(0, w):
        now_w = h * i
        if n > now_w and n <= (h * (i + 1)):
            return str(n - (h * i)) + str(i + 1).zfill(2)

for _ in range(T):
    h, w, n = tuple(map(int, input().split()))
    print(get_room(h, w, n))
