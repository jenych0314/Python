import sys
input = sys.stdin.readline


def solve1():
    x, y, w, h = map(int, input().split())

    up = h-y
    down = y
    left = x
    right = w-x

    print(min(up, down, left, right))


def solve2():
    x, y, w, h = map(int, input().split())
    distance = [h-y, y, x, w-x]
    print(min(distance))


solve2()
