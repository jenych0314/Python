import sys

N = int(sys.stdin.readline().strip())

num_lst = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())

find_lst = list(map(int, sys.stdin.readline().strip().split()))

# 첫 번째, 정렬하면서 갯수도 따로 센다.
# 두 번째, 찾을 때 여러번 찾는다.
