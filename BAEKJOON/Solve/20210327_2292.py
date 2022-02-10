n = int(input())

n -= 1
cnt, check = 1, 0

while n > 0:
    check += 6
    n -= check
    cnt += 1

print(cnt)