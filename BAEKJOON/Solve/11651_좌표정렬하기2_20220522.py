import sys
input = sys.stdin.readline

n = int(input())

coordinate = dict()

for i in range(n):
    x, y = map(int, input().split())
    if y not in coordinate:
        coordinate[y] = [x]
    else:
        coordinate[y].append(x)

for y in sorted(coordinate.keys()):
    for x in sorted(coordinate[y]):
        print(x, y)
