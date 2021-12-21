def hanoi(n, start, mid, end):
    if n == 1:
        return print('{}: {} -> {}'.format(n, start, end))
        
    hanoi(n-1, start, end, mid)
    print('{}: {} -> {}'.format(n, start, end))
    hanoi(n-1, mid, start, end)

n = int(input())

hanoi(n, 'A', 'B', 'C')