def main(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_date
    else:
        month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_date

week = '일월화수목금토'

year, month, day = map(int, input().split())
n = 0

for i in range(1, year):
    n += sum(main(i))

temp = main(year)
for j in range(month-1):
    n += temp[j]

n += day

print(week[n%7])