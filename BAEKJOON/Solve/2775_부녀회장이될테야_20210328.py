import sys
input = sys.stdin.readline


def fac(num):
    if num == 0 or num == 1:
        return 1
    return num * fac(num - 1)


def comb(n1, n2):
    if n2 == 0:
        return 1
    return fac(n1) / (fac(n2) * fac(n1 - n2))


t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    resident = int(comb(k+n, k+1))
    print(resident)
