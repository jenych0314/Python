import time
import random

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

    if idx == -1:
        print("No such numbers: ", target)
    else:
        print("Target {} is at Index {}".format(target, idx))

nums = list(map(int, input().split()))
nums.sort()

target = int(input())
print(binary_search(nums, target))