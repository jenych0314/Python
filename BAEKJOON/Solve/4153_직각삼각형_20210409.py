import sys
input = sys.stdin.readline


def solve1():
    while True:
        nums = list(map(int, input().split()))
        if sum(nums) == 0:
            break
        nums.sort()

        if nums[0]**2 + nums[1]**2 == nums[-1]**2:
            print('right')
        else:
            print('wrong')


def solve2():
    while (True):
        nums = list(map(int, input().split()))
        if sum(nums) == 0:
            break
        nums.sort()

        print('right') if (nums[0]**2 + nums[1] **
                           2 == nums[-1]**2) else print('wrong')


solve2()
