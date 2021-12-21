import sys

N = int(input())

dic = dict()

for i in range(N):
    num = int(sys.stdin.readline().strip())

    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for num, cnt in sorted(dic.items()):
    for n in range(cnt):
        print(num)