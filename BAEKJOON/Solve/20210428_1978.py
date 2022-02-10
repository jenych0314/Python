import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

if 1 in nums:
    nums.remove(1)

arr = [True for i in range(max(nums) + 1)]

for i in range(2, int(max(nums)**0.5 + 1)):
    if arr[i]:
        for j in range(2, max(nums)//i + 1):
            arr[i*j] = False

cnt = 0
for num in nums:
    if arr[num]:
        cnt += 1
    
print(cnt)