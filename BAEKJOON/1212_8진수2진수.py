def oct2bin(char_num):
    result = ''

    char_num = int(char_num)

    for i in range(3):
        result += str(char_num % 2)
        char_num = char_num // 2

    return result[::-1]


oct_num = input()

result = ''
for c in oct_num:
    result += oct2bin(c)

result = int(result)

print(result)
