def gcd(num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)

    if small == 0:
        return big

    return gcd(small, big % small)


x, y = map(int, input().split())

gcdNum = gcd(x, y)

m, n = x/gcdNum, y/gcdNum
answer = 0

if m == n:
    answer = x
elif m == 1 or n == 1:
    answer = n * m * gcdNum
else:
    answer = gcdNum * (m + n - 1)

print(int(answer))
