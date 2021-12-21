import sys
# import numpy as np
sys.setrecursionlimit(99999999)

# col, row, t = map(int, input().split())

def solution(col, row, t):
    lst = scores
    # for y in range(col):
    #     o = list(map(int, sys.stdin.readline().split()))
    #     lst.append(o)

    resized = []
    for y in range(col):
        temp = []
        for x in range(row//3):
            team = lst[y][3*x:3*x + 3]
            average = sum(team)/3
            if average < t:
                average = 0
            temp.append(average)
        resized.append(temp)

    # for y in range(col):
    #     for x in range(row//3):
    #         if resized[y][x] < t:
    #             resized[y][x] = 0

    for y in range(col):
        for x in range(row//3):
            pass

col, row, t = 4, 6, 100
scores = [
    [100, 150, 0, 90, 80, 150],
    [100, 200, 200, 3, 5, 7],
    [50, 70, 0, 200, 300, 150],
    [110, 120, 130, 70, 80, 100]
]