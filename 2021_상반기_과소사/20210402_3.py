year, month, day = map(int, input().split())
total_days = 0

def is_leap_year(year):
    return ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))

#년도별 일수 더하기 (1, year - 1)
for i in range(1, year):
    total_days += 365 if not (is_leap_year(i)) else 366

dpm = (0, 31, (28 if not (is_leap_year(year)) else 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

#월별 일수 더하기
total_days += sum(dpm[1:month])

#날짜에 대한 일수 더하기
total_days += (day - 1)

#출력
print('월화수목금토일'[total_days%7])