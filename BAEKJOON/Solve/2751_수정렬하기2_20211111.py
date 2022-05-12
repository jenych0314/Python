import sys
input = sys.stdin.readline


def partition(data, start, end):
    pivot = data[end]
    curr_small_loc = start

    for i in range(start, end + 1):
        if data[i] <= pivot:
            data[i], data[curr_small_loc] = data[curr_small_loc], data[i]
            curr_small_loc += 1

    return curr_small_loc - 1


def quicksort(data, start, end):
    if start >= end:
        return

    pivot_pos = partition(data, start, end)

    quicksort(data, start, pivot_pos - 1)
    quicksort(data, pivot_pos + 1, end)


N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

quicksort(lst, 0, N - 1)

for val in lst:
    print(val)
