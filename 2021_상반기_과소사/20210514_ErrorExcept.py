def divide (m, n):#주로 백엔드
    result = -1
    try:
        result = m/n
    except ZeroDivisionError:
        print('it can\'t divide with Zero')
    finally:
        return result

def divideCheck(m,n):#주로 프런트엔드
    if n == 0:
        print('it can\'t divide with Zero')
        return -1
    return m/n

print(divide(2,0))
print(divide(2,1))