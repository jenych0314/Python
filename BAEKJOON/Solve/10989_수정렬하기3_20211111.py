import sys
input = sys.stdin.readline


def solve1():
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


def solve2():
    n = int(input())
    dic = dict()
    for i in range(1, 10001):
        dic.setdefault(i, 0)

    for i in range(n):
        num = int(input())
        dic[num] += 1

    for k, v in dic.items():
        if v == 0:
            continue
        else:
            for i in range(v):
                print(k)


solve2()
