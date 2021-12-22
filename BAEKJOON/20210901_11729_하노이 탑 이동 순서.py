def hanoi(n, left, mid, right):
    if n == 1:
        return print("{} {}".format(left, right))

    hanoi(n-1, left, right, mid)
    print("{} {}".format(left, right))
    hanoi(n-1, mid, left, right)


n = int(input())

print(2**n - 1)
hanoi(n, "1", "2", "3")
