import sys
input = sys.stdin.readline


def gcd(num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)

    if small == 0:
        return big

    return gcd(small, big % small)


a, b = map(int, input().split())

print(gcd(a, b))
print(abs(a * b) // gcd(a, b))
