def body(start, stop):
    for i in range(start, stop):
        result = i
        temp = str(i)
        for j in range(len(temp)):
            result += int(temp[j])
        if result == n:
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