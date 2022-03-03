from math import sqrt

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    d = int(sqrt(y-x))
    if y-x == d**2:
        print(2*d - 1)
    elif d**2 < y-x <= d**2 + d:
        print(2*d)
    elif d**2 + d < y-x < (d+1)**2:
        print(2*d + 1)