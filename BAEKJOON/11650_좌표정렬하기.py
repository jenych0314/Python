import sys
input = sys.stdin.readline

n = int(input())

coordinate = dict()

for i in range(n):
    x, y = int(input().split())
    if x not in coordinate:
        coordinate[x] = [y]
    else:
        pass
