import statistics
import sys

def solution1():
    N = int(sys.stdin.readline().strip())

    num_lst = []

    for i in range(N):
        num = int(sys.stdin.readline().strip())
        num_lst.append(num)

    num_lst.sort()

    arithmetic_mean = round(statistics.mean(num_lst))
    median_num = statistics.median(num_lst)
    mode_num_lst = statistics.multimode(num_lst)
    num_range = num_lst[-1] - num_lst[0]

    print(arithmetic_mean)
    print(median_num)
    if len(mode_num_lst) > 1:
        print(mode_num_lst[1])
    else:
        print(mode_num_lst[0])
    print(num_range)

def quick_sort(arr):
    if len(arr) <= 1:  # arr의 크기가 1 이하일 경우. 재귀함수의 종료 조건.
        return arr
    
    pivot = len(arr) // 2
    front_arr, pivot_arr, back_arr = [], [], []

    for val in arr:  # pivot을 기준으로 arr을 쪼갬
        if val < arr[pivot]:
            front_arr.append(val)
        elif val > arr[pivot]:
            back_arr.append(val)
        else:
            pivot_arr.append(val)

    # 재귀함수. 쪼갠 arr을 각각 다시 새로운 pivot을 뽑아 더 쪼갬. 작은 숫자의 arr부터 앞으로 오게끔 각각의 arr을 더함.
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

def counting_sort(arr, max_num):
    counting_arr = [0] * (max_num + 1)

    for i in arr:
        counting_arr[i] += 1
    
    print('1\n', counting_arr)

    for i in range(max_num):
        counting_arr[i + 1] += counting_arr[i]
    
    print('2\n', counting_arr)

    output_arr = [-1] * len(arr)

    for i in arr:
        print(counting_arr[i], i, end= ' -> ')
        output_arr[counting_arr[i] - 1] = i
        counting_arr[i] -= 1
        print(counting_arr[i], i)
        print('out:', output_arr)
    
    return output_arr

N = int(sys.stdin.readline().strip())

MAX_NUM = 10
negative_num_lst, positive_num_lst = [], []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num >= 0:
        positive_num_lst.append(num)
    else:
        negative_num_lst.append(num)

print('negative')
sorted_negative_num_lst = counting_sort(negative_num_lst, MAX_NUM)
print('positive')
sorted_positive_num_lst = counting_sort(positive_num_lst, MAX_NUM)
num_lst = sorted_negative_num_lst + sorted_positive_num_lst

arithmetic_mean = round(sum(num_lst) / N)
median_num = num_lst[N // 2]
mode_num_lst = []
num_range = num_lst[-1] - num_lst[0]

print(num_lst)