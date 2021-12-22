def answer(n, lst):
    arr = []

    for i in range(n):
        k = 0
        for j in range(n):
            if (lst[i][0] < lst[j][0]) and (lst[i][1] < lst[j][1]):
                k += 1
        arr.append((i, k))

    return arr


n = int(input())
lst = []

for i in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

temp = answer(n, lst)

for i, k in temp:
    print(k+1, end=" ")
