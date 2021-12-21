def solution(arr):
    answer = True
    s = set(arr)
    return len(s) == len(arr) and max(arr) == len(arr) and min(arr) == 1