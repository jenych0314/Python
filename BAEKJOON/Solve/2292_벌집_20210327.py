import sys
input = sys.stdin.readline


def solve1():
    n = int(input())

    n -= 1
    cnt, check = 1, 0

    while n > 0:
        check += 6
        n -= check
        cnt += 1

    print(cnt)


def solve2():
    n = int(input()) - 1

    cnt, decrease = 1, 0

    while n > 0:
        decrease += 6
        n -= decrease
        cnt += 1

    print(cnt)


solve2()
