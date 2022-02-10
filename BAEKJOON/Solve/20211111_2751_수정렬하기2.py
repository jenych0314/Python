import sys

N = int(input())

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline().strip()))

for i in sorted(lst):
    print(i)