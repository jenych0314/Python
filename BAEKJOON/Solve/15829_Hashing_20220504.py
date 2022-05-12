import sys
input = sys.stdin.readline


def solve():
    r, M = 31, 1234567891
    L = int(input())
    string = input()

    result = 0

    for i in range(L):
        result += ((ord(string[i]) - ord('a') + 1) * (r ** i)) % M

    print(result % M)


solve()
