import collections

def solution(v):
    answer = []
    lst = list(zip(*v))

    for point in lst:
        x = collections.Counter(point)

        answer.extend([key for key, value in x.items() if value == 1])
        
    return answer