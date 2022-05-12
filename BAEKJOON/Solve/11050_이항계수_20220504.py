import sys
input = sys.stdin.readline

N, K = map(int, input().split())

memo = dict()


def factorial(num):
    global memo

    if num in memo:
        return memo[num]
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
            memo[i] = result
        return result


def combination(num1, num2):
    if num2 == 0:
        return 1

    return factorial(num1) / (factorial(num2) * factorial(num1 - num2))


print(int(combination(N, K)))
