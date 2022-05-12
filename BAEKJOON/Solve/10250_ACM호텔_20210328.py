import imp


import sys
input = sys.stdin.readline


def solve1():
    t = int(input())

    for i in range(t):
        h, w, n = map(int, input().split())
        # h = 층, w = 층당 방개수, n = 몇 번째 손님
        x = divmod(n, h)  # n/h => (몫, 나머지)
        if x[1] == 0:
            print('%d%02d' % (h, x[0]))
        else:
            print('%d%02d' % (x[1], x[0]+1))


def solve2():
    T = int(input())

    for i in range(T):
        h, w, n = map(int, input().split())
        Y = n % h if (n % h != 0) else h
        X = n // h + 1 if (n % h != 0) else n // h
        print("%d%02d" % (Y, X))


solve2()
