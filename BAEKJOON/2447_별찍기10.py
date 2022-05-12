def recursive_func(n):
    global lst

    if n == 3:
        pass

    for i in range(n//3):
        for j in range(n//3):
            pass

    recursive_func(n//3)

N = 27
# N = int(input())

lst = [['*' for i in range(N)] for j in range(N)]

recursive_func(N)