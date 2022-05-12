import sys
input = sys.stdin.readline

n = int(input())  # n>0

cnt = 0
i = 1

while cnt != n:
    i += 1
    if '666' in str(i):
        cnt += 1

print(i)
