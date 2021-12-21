year = 0
balance = 1000000

while balance < 2000000:
    year += 1
    balance = int(balance * 1.05)
else:
    print('{}년동안 저축하시면 {}를 받습니다.'.format(year, balance))
#무엇을 반복할 것인가
#무엇이 바뀔 것인가
#반복의 종료 조건은 무엇인가