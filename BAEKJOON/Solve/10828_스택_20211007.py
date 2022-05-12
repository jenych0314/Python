import sys

N = int(sys.stdin.readline())

commands = ['push', 'pop', 'size', 'empty', 'top']
arr = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == commands[0]:  # push
        arr.append(command[1])
    elif command[0] == commands[1]:  # pop
        print(arr.pop()) if arr else print(-1)
    elif command[0] == commands[2]:  # size
        print(len(arr))
    elif command[0] == commands[3]:  # empty
        print(0) if arr else print(1)
    else:  # top
        print(arr[-1]) if arr else print(-1)
