import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
# a = 올라가는 높이, b = 미끄러지는 높이, v = 총 높이
temp = (divmod((v - a), (a - b)))

if temp[1] != 0:
    ans = temp[0] + 2
else:
    ans = temp[0] + 1

print(ans)
