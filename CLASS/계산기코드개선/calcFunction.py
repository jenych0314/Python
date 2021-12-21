from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error'
    return r

def dec2bin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error'
    return r

def bin2dec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error'
    return r

def dec2roman(numStr):
    try:
        n = int(numStr)

        if n <= 0 or n >= 10000:
            return 'Error'
        
        romans = [
            (9000, 'FMF'), (5000, 'F'), (4000, 'MF'), (1000, 'M'),
            (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        result = ''
        for value, letters in romans:
            while n >= value:
                result += letters
                n -= value
        
        return result
    except:
        return 'Error'

def roman2dec(numStr):
    try:
        if numStr.isnumeric():
            return 'Error'

        numStr = numStr.upper()

        romans = {
            'F': 5000, 'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1
        }

        first = numStr[0]
        result = romans[first]

        for i in range(1, len(numStr)):
            last = first
            first = numStr[i]

            if(romans[last] >= romans[first]):
                result += romans[first]
            else:
                result += romans[first] - 2 * romans[last]

        return result
    except:
        return 'Error'

if __name__ == '__main__':

    from random import *

    numlst = [randint(0, 9999) for x in range(100)]
    lst = []
    for num in numlst:
        letter = dec2roman(str(num))
        lst.append((num, letter))

    for num, letter in lst:
        print(num, letter, roman2dec(letter))