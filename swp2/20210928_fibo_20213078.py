import time

n = 35

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

ts = time.time()

for i in range(n):
    print(fibo(i))

print(time.time() - ts)

cnt = 0
dic = {}

def fibo(n):
    global cnt, dic
    cnt += 1

    if n in dic:
        return dic[n]

    if n <= 1:
        dic[n] = n
    else:
        dic[n] = fibo(n - 1) + fibo(n - 2)    
    return dic[n]

ts = time.time()

for i in range(n):
    print(fibo(i))

print(time.time() - ts)

def fibo(n):
    if n <= 1:
        return n
        
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        
    return b

ts = time.time()

for i in range(n):
    print(fibo(i))

print(time.time() - ts)