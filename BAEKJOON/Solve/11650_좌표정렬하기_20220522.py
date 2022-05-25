import sys
input = sys.stdin.readline

n = int(input())

coordinate = dict()

for i in range(n):
    x, y = map(int, input().split())
    if x not in coordinate:
        coordinate[x] = [y]
    else:
        coordinate[x].append(y)

for x in sorted(coordinate.keys()):
    for y in sorted(coordinate[x]):
        print(x, y)
