import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = []

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            # print(i, j, k)
            if nums[i] + nums[j] + nums[k] > m:
                continue
            else:
                result.append(sum((nums[i], nums[j], nums[k])))

print(max(result))
