def body(start, stop):
    for i in range(start, stop):
        result = i
        char_num = str(i)
        for c in char_num:
            result += int(c)
        # for j in range(len(char_num)):
        #     result += int(char_num[j])
        if result == stop:
            return i
    return 0


def answer(n):
    x = 9 * len(str(n))
    if x >= n:
        return body(0, n)
    else:
        return body(n-x, n)


n = int(input())
print(answer(n))
