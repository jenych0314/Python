def binary_search_recursive(lst, start, end, target):
    mid = (start + end) // 2

    if start > end:
        return -1
    
    if target == lst[mid]:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, start, mid - 1, target)
    else:
        return binary_search_recursive(lst, mid + 1, end, target)

def binary_search_iterative(lst, target):
    start = 0
    end = len(lst) - 1
    idx = -1

    while(start <= end):
        mid = (start + end) // 2
        if lst[mid] == target:
            idx = mid
            break
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return idx

lst = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

start = 0; end = len(lst); target = 17
index = binary_search_recursive(lst, start, end, target)
print(index)

index = binary_search_iterative(lst, target)
print(index)