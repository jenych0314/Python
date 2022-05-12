import sys


def binary_search(nums, target):
    lower = 0
    upper = len(nums) - 1
    idx = -1

    while (lower <= upper):
        middle = int((lower + upper) // 2)
        if nums[middle] == target:
            idx = middle
            break
        elif nums[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

    return 0 if (idx == -1) else 1


N = int(sys.stdin.readline().strip())

num_lst = list(map(int, sys.stdin.readline().strip().split()))
num_lst.sort()  # 나중에는 정렬하는 것도 직접해보는 걸로 하자.

M = int(sys.stdin.readline().strip())

find_lst = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
    print(binary_search(num_lst, find_lst[i]))
