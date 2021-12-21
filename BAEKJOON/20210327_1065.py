def ans(num):
    num = str(num)
    if len(num) < 3:
        return True
    else:
        d = int(num[1]) - int(num[0])
        for i in range(1, len(num) - 1):
            if d != (int(num[i + 1]) - int(num[i])):
                return False
        else:
            return True

n = int(input())
cnt = 0

for i in range(1, n + 1):
    if ans(i) == True:
        cnt += 1

print(cnt)