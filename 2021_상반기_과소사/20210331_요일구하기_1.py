def main(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

week = ['일', '월', '화', '수', '목', '금', '토']

year, month, day = map(int, input().split())
n = 0

for i in range(1, year):
    if main(i) == True:#leap year
        month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n += sum(month_date)
    else:
        month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n += sum(month_date)

for j in range(month-1):
    if main(year) == True:#leap year
        month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n += month_date[j]
    else:
        month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n += month_date[j]

n += day

print(week[n%7])