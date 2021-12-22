n = int(input())

lst = [['*' for i in range(n)] for j in range(n)]

for a in range(n//3):
    for b in range(n//3):
        for i in range(n//3):
            for j in range(n//3):
                sublst = lst[i + a*n//3][j + b*n//3]
                idx = a*3 + b + 1
                if idx == 5:
                    pass

for i in range(n):
    for j in range(n):
        print(lst[i][j], end=', ')
    print()
