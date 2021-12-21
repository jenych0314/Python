# for i in range(10):
#     for j in range(10):
#         print('*', end='')
#     print()

# for i in range(10):
#     print('*'*10)

n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    print()

for i in range(1, n+1):
    print('*'*i)