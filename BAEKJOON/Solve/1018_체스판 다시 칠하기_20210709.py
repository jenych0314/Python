import copy
import sys
input = sys.stdin.readline


result = []


def compare(arr1, arr2):
    global result

    cnt1 = 0
    cnt2 = 0

    for i in range(8):
        for j in range(8):
            if arr1[i][j] == arr2[i][j]:
                cnt1 += 1
            else:
                cnt2 += 1

    return result.append(min(cnt1, cnt2))


n, m = map(int, input().split())
arr = [list(map(str, input())) for row in range(n)]

board = [["B" if i % 2 == 0 else "W" for i in range(8)] if j % 2 == 0 else [
    "W" if i % 2 == 0 else "B" for i in range(8)] for j in range(8)]

for i in range(n - 7):
    for j in range(m - 7):
        temp = [row[j: j + 8] for row in copy.deepcopy(arr)[i: i + 8]]
        compare(temp, board)

print(min(result))
