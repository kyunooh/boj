T = int(input())
N = sorted(list(map(int, input().split())))

def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
     
    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
     

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    return True

max = 0

def abs(x):
    if x < 0:
        return -x
    return x

while next_permutation(N):
    temp = 0
    for x in range(T - 1):
        temp += abs(N[x] - N[x+1])
    if temp > max:
        max = temp

print(max)



