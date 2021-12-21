cnt = 0
memo = {}

def fibo(n):
    global cnt
    cnt += 1
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())

print(fibo(n))
print(cnt)