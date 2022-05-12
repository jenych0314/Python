import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 0  # a = 3kg, b = 5kg

a = n // 3
ans = ()

while a >= 0:
    b = (n - 3 * a) / 5
    temp = b - int(b)
    if temp == 0:
        ans = (a, b)
    a -= 1

if len(ans) != 0:
    print(int(sum(ans)))
else:
    print(-1)
