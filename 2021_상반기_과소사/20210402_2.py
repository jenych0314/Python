import datetime

year, month, day = map(int, input().split())
total_days = 0

print('월화수목금토일'[datetime.date(year, month, day).weekday()])

#년도별 일수 더하기 (1, year - 1)
for i in range(1, year):
    total_days += 365 if not (i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0)) else 366

#월별 일수 더하기
#1, 3, 5, 7, 8, 10, 12 = 31
#2 = 28 or 29
#나머지 = 30
for i in range(1, month):
    if i in [1,3,5,7,8,10,12]:
        total_days += 31
    elif i == 2:
        total_days += 28 if not (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else 29
    else:
        total_days += 30

#날짜에 대한 일수 더하기
total_days += (day - 1)

#출력
print('월화수목금토일'[total_days%7])