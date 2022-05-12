import sys
input = sys.stdin.readline


def solve1():
    minNum, maxNum = map(int, input().split())

    arr = [i ** 2 for i in range(2, int(maxNum ** 0.5) + 1)]
    # print(arr)

    if arr[0] > minNum:
        cnt = arr[0] - minNum
        minRange = arr[0] + 1
    else:
        cnt = 0
        minRange = minNum

    for num in range(minRange, maxNum + 1):
        for sqareNum in filter(lambda x: x <= num, arr):
            # print(num, sqareNum)
            if num % sqareNum == 0:
                break
        else:
            # print("else")
            cnt += 1

    print(cnt)


def solve2(MIN, MAX):
    answer = MAX - MIN + 1
    arr = [False] * (MAX - MIN + 1)
    i = 2
    while i * i <= MAX:
        square_number = i * i  # 제곱수
        # remain
        # 제곱수가 딱 나누어 떨어지면 상관없지만 그게 아니라면 소수점이 버림 처리 된다.
        # 그래서 remain으로 그 값을 보정해준다.
        remain = 0 if MIN % square_number == 0 else 1
        j = MIN // square_number + remain  # 제곱수로 나눈 몫 => 배수
        while square_number * j <= MAX:
            # 제곱수의 j배 (에라토스테네스의 체)
            if not arr[square_number * j - MIN]:
                arr[square_number * j - MIN] = True
                answer -= 1
                j += 1
                # 배수 점점 증가
        i += 1
    print(answer)


def solve3():
    a, b = map(int, input().split())
    arr = [1] * (b - a + 1)
    for i in range(2, int(b ** 0.5) + 1):
        t = i ** 2
        for j in range(a // t * t, b + 1, t):
            if j - a >= 0 and arr[j - a]:
                arr[j - a] = 0
    print(arr.count(1))


solve3()
