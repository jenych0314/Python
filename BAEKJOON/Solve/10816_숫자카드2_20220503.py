import sys
input = sys.stdin.readline


def solve1():
    N = int(input())
    haved_dic = dict()

    for haved_card in list(map(int, input().split())):
        if haved_card in haved_dic:
            haved_dic[haved_card] += 1
        else:
            haved_dic[haved_card] = 1

    M = int(input())
    find_lst = list(map(int, input().split()))

    for find_card in find_lst:
        if find_card in haved_dic:
            print(haved_dic[find_card], end=' ')
        else:
            print(0, end=' ')


solve1()
