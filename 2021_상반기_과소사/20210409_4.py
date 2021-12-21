# 8, 4, 9, 5

arr = [8, 4, 9, 5]
# small = arr[0]

# for i in range(1, len(arr)):
#     if small > arr[i]:
#         small = arr[i]

# print(small)

large = arr[0]

for i in range(1, len(arr)):
    if large < arr[i]:
        large = arr[i]

print(large)