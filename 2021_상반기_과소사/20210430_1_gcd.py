def gcd (num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)
    if small == 0:
        return big
    return gcd (small, big%small)

num1, num2 = map(int, input().split())

print(gcd(num1, num2))