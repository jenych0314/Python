cnt = 0

def fibo(n):
    global cnt
    cnt += 1
    
    if n <= 1:
        return n
    else:
       return fibo(n-2) + fibo(n-1)

n = int(input())

print(fibo(n))
print(cnt)