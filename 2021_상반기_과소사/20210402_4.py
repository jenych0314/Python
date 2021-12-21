year, month, day = map(int, input().split())
total_days = 0

def is_leap_year(year):
    return ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))

leap_years = len(list(filter(is_leap_year, range(1, year))))
not_leap_years = year - 1 - leap_years

total_days += leap_years*366 + not_leap_years*365

dpm = (0, 31, (28 if not (is_leap_year(year)) else 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

#월별 일수 더하기
total_days += sum(dpm[1:month])

#날짜에 대한 일수 더하기
total_days += (day - 1)

#출력
print('월화수목금토일'[total_days%7])