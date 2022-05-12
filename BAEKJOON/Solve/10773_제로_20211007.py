import sys

K = int(sys.stdin.readline())
lst = []

for i in range(K):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        del lst[-1]
    else:
        lst.append(tmp)

print(sum(lst))
