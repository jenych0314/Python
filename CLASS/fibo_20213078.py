from math import sqrt
import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

cnt = 0
dic = {}

def fibo_memo(n):
    global cnt, dic
    cnt += 1

    if n in dic:
        return dic[n]

    if n <= 1:
        dic[n] = n
    else:
        dic[n] = fibo_memo(n - 1) + fibo_memo(n - 2)    
    return dic[n]

def fibo_iterative(n):
    if n <= 1:
        return n
        
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        
    return b

def fibo_progression(n):
    ans = (1 / sqrt(5)) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n)
    return int(ans)

# n = random.randint(1, 500)
n = 40
print('n: ', n)

# fibo
ts = time.time()
print('fibo(%d) = %d' %(n, fibo(n)))
print(time.time() - ts)

# fibo_memo
ts = time.time()
print('fibo(%d) = %d' %(n, fibo_memo(n)))
print(time.time() - ts)

# fibo_iterative
ts = time.time()
print('fibo(%d) = %d' %(n, fibo_iterative(n)))
print(time.time() - ts)

# fibo_progression
ts = time.time()
print('fibo(%d) = %d' %(n, fibo_progression(n)))
print(time.time() - ts)