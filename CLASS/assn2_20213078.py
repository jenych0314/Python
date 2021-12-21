import time
import random

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def binary_search_iterative(lst, target):
    lower = 0
    upper = len(lst) - 1
    idx = -1

    while (lower <= upper):
        middle = int((lower + upper) // 2)
        if lst[middle] == target:
            idx = middle
            break
        elif lst[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

    return idx

def binary_search_recursive(lst, target, lower, upper):
    if lower > upper:
        return -1
    
    middle = int((lower + upper) // 2)

    if lst[middle] == target:
        return middle
    elif lst[middle] < target:
        return binary_search_recursive(lst, target, middle + 1, upper)
    else:
        return binary_search_recursive(lst, target, lower, middle - 1)

def random_list(size):
    lst = [random.randint(0, 999999) for i in range(size)]
    return lst

numbers_lst_size = int(input('Enter numbers list size: '))

numbers = random_list(numbers_lst_size)
numbers = sorted(numbers)

targets_lst_size = int(input('Enter target numbers list size: '))

targets = random_list(targets_lst_size)

# binary search - iterative
ts = time.time()

cnt = 0
for target in targets:
    idx = binary_search_iterative(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("binary_search_iterative %d: not found %d times %.6f" % (targets_lst_size, cnt, ts))

# binary search - recursive
ts = time.time()

cnt = 0
for target in targets:
    idx = binary_search_recursive(numbers, target, 0, len(numbers))
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("binary_search_recursive %d: not found %d times %.6f" % (targets_lst_size, cnt, ts))

# sequential search
ts = time.time()

cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d times %.6f" % (targets_lst_size, cnt, ts))