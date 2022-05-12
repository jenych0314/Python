n = int(input())

arr = [int(c) for c in input()]
arr2 = arr[:]

cnt = 0
# first place O
for i in range(1, n):
    if arr[i - 1] == 0:
        # arr[i - 1] = 1 if arr[i - 1] == 0 else 0
        arr[i - 1] ^= 1
        arr[i] ^= 1
        if i + 1 < n:
            arr[i + 1] ^= 1
        cnt += 1
# check
if arr[-1] == 0:
    cnt = 999999

# first place X
arr2[0] ^= 1
arr2[1] ^= 1
cnt2 = 1

for i in range(1, n):
    if arr2[i - 1] == 0:
        # arr[i - 1] = 1 if arr[i - 1] == 0 else 0
        arr2[i - 1] ^= 1
        arr2[i] ^= 1
        if i + 1 < n:
            arr2[i + 1] ^= 1
        cnt2 += 1

if arr2[-1] == 0:
    cnt = 999999

print(min(cnt, cnt2))