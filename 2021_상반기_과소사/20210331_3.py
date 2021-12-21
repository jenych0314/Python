year = 0
result = 1000000
balance = 1000000

while result < 2000000:
    year += 1
    result += int(balance * 0.05)
else:
    print('{}년동안 저축하시면 {}를 받습니다.'.format(year, result))