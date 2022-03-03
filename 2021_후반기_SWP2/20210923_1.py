#1
numbers = list(map(int, input("Enter list of numbers: ").split()))

min_val = 2**15 - 1

for num in numbers:
    if min_val > num:
        min_val = num

print(min_val)


#2
numbers = list(map(int, input("Enter list of numbers: ").split()))

try:
    min_val = numbers[0]

    for num in numbers:
        if min_val > num:
            min_val = num
except IndexError:
    print("IndexError")

print(min_val)


#3
numbers = list(map(int, input("Enter list of numbers: ").split()))

try:
    min_val = numbers[0]
    min_idx = 0
    for i in range(1, len(numbers)):
        if min_val > numbers[i]:
            min_val = numbers[i]
            min_idx = i
except IndexError:
    print("IndexError")

print(min_val, min_idx)


#4
numbers = list(map(int, input("Enter list of numbers: ").split()))

try:
    max_val = numbers[0]
    max_idx = 0
    for i in range(1, len(numbers)):
        if max_val < numbers[i]:
            max_val = numbers[i]
            max_idx = i
except IndexError:
    print("IndexError")

print(max_val, max_idx)