import math

def prime_nums(n):
    arr = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i]:
            for j in range(2, n//i + 1):
                arr[i*j] = False

    return [i for i in range(2, len(arr)) if arr[i]]

prime = prime_nums(10000)

t = int(input())

for i in range(t):
    n = int(input())
    
    for i in range(n//2, 1, -1):
        if (n - i in prime) and (i in prime):
            print(i, n - i)
            break