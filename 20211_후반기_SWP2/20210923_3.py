def solution1(num):
    ans = 0

    num = str(num)

    for n in num:
        ans += int(n)

    return ans

def solution2(num):
    ans = 0
    while num != 0:
        ans += num%10
        num = num//10
    return ans

def solution3(num):
    return sum([int(i) for i in str(num)])

num = int(input())
print(solution1(num))
print(solution2(num))
print(solution3(num))