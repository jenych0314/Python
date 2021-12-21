# for i in range(1, 10):
#     print('{} * {} = {}'.format(2, i, 2*i))

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{} * {} = {}'.format(i, j, i*j))
#     print()

# for i in range(1, 10):
#     for j in range(1, 10):
#         for k in range(1, 10):
#             print('{} * {} * {} = {}'.format(i, j, k, i*j*k))
#     print()

i, j = 1, 1
while i < 10:
    j = 1
    while j < 10:
        print('{} * {} = {}'.format(i, j, i*j))
        j += 1
    i += 1
    print()