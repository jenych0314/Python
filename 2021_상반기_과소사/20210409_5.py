import math

n = int(input())

arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i]:# == True:
        for j in range(2, n//i + 1):
            arr[i*j] = False

print([i for i in range(2, len(arr)) if arr[i]])