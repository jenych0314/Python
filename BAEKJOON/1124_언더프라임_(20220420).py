import sys
input = sys.stdin.readline


def isUnderPrime(num):
    global arr, B

    cnt = 0

    for i in range(2, B + 1):
        if arr[i] and num % i == 0:
            cnt += 1
            num /= i
            while(num % i == 0):
                cnt += 1
                num /= i

        if i > num:
            break

    return arr[cnt]


def solve1():
    A, B = map(int, input().split())

    arr = [True for i in range(B + 1)]
    for i in range(2, int(B ** 0.5) + 1):
        if arr[i]:
            for j in range(i, B // i + 1):
                arr[i * j] = False
    arr[0] = arr[1] = False

    numCount = 0
    for i in range(A, B + 1):
        if (isUnderPrime(i)):
            numCount += 1

    print(numCount)


def solve2():
    a, b = map(int, input().split())
    arr1 = [True for i in range(100001)]
    arr1[1] = False

    m = int(100000 ** 0.5)
    for i in range(2, m + 1):
        if arr1[i]:
            for k in range(i, 100001):
                if i * k > 100000:
                    break
                arr1[i * k] = False
        if i * (i + 1) > 100000:
            break

    arr2 = [0 for i in range(b + 1)]

    for i in range(1, b + 1):
        if arr1[i]:
            arr2[i] = 1
    for i in range(2, b + 1):
        for j in range(2, b + 1):
            if i * j > b:
                break
            if arr1[j]:
                arr2[i * j] = arr2[i] + 1

    cnt = 0
    for i in range(a, b + 1):
        if arr1[arr2[i]]:
            cnt += 1

    print(cnt)


solve2()
