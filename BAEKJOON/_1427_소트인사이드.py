from sys import stdin

def quick_sort(string):
    if len(string) <= 1:
        return string
    
    pivot = string[len(string) // 2]
    small, middle, big = '', '', ''

    for char in string:
        if char > pivot:
            big += char
        elif char < pivot:
            small += char
        else:
            middle += char
    
    return quick_sort(small) + quick_sort(middle) + quick_sort(big)

def quick_sort(string):
    pivot = string[len(string) // 2]
    small, middle, big = '', '', ''

    while True:
        pass

N = stdin.readline().strip()

temp = quick_sort(N)

print(temp[::-1])