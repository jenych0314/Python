def fibo(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b

    return b


T = int(input())

for i in range(T):
    N = int(input())
    if N == 0:
        print('1 0')
    else:
        print(fibo(N - 1), fibo(N))
