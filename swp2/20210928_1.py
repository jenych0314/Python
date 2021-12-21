#1 
upper = int(input())
sum_val = 0

for i in range(1, upper + 1):
    sum_val += i

print(sum_val)


#2
def recursive_sum(n):
    return 1 if n == 1 else recursive_sum(n - 1) + n

print(recursive_sum(upper))


#3
numbers = map(int, input().split())

def recursive_arr_sum(nums, k):
    if k == 0:
        return nums[0]
    return recursive_arr_sum(nums, k - 1) + nums[k]

print(recursive_arr_sum(numbers, len(numbers) - 1))