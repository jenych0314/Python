x = int(input())
cnt = 1

while x > cnt:
    x -= cnt
    cnt += 1

if cnt%2 == 1:
    a, b = cnt, 1#분모, 분자
    for i in range(x - 1):
        a -= 1
        b += 1
else:
    a, b = 1, cnt#분모, 분자
    for i in range(x - 1):
        a += 1
        b -= 1

print('%d/%d'%(a, b))