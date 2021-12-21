def solution(arr):
    answer = True

    arr.sort()

    for i in range(len(arr)):
        if arr[i] != i+1:
            return False
    
    return answer