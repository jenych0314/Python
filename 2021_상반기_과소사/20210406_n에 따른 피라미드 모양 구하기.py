n = int(input('pls enter a natural number: '))

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i - 1):
        print('O', end='')
    print()
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i - 1):
        print('O', end='')
    print()