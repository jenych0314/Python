def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-2) + fibonacci_sequence(n-1)

n = int(input())

print(fibonacci_sequence(n))