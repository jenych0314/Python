# 1. 버블정렬을 구현하시오
# 2. 구현한 버블정렬과 sort()함수와의 처리 시간을 비교하시오
# 버블정렬 구현
# n개의 정수로 구성된 리스트 a가 주어졌을 때 작은 값부터 순서대로 정렬하는 프로그램을 작성하기오
# 두 수를 비교하여 큰 수를 뒤로, 작은 수를 앞으로 이동
# [0, n-1] 중 가장 큰 수를 찾아 a[n-1]로 이동시킴
# [0, n-2] 중 가장 큰 수를 찾아 a[n-2]로 이동시킴
# [0, 1] 중 가장 큰 수를 찾아 a[1]로 이동시킴
import sys
import time
import random

def bubble_sort(nums):
    for i in range(1, len(nums)):#list index out of range 오류 안나게 할려고 1부터 시작했다.
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# arr = list(map(int, sys.stdin.readline().split()))
arr = list(range(1, 10001))
random.shuffle(arr)

start_time1 = time.time() 
result = bubble_sort(arr)
print('내가 구현한 버블정렬: ', time.time() - start_time1)

start_time2 = time.time()
result = sorted(arr)
print('파이썬에서 제공하는 sort함수: ', time.time() - start_time1)

#8 5 2 7 4 1 9 6 3 10
#성공시켰는데 왜 되는건지 모르겠습니다...