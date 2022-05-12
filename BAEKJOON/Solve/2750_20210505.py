def bubble_sort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in bubble_sort(arr):
    print(i)