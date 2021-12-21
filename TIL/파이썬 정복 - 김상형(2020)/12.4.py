import calendar
import time
import sys

if len(sys.argv) == 1:
    t = time.time()
    tm = time.localtime(t)
    calendar.prmonth(tm.tm_year, tm.tm_mon)
elif len(sys.argv) == 2:
    print(calendar.calendar(int(sys.argv[1])))
elif len(sys.argv) == 3:
    calendar.prmonth(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("인수는 2개 이하여야 합니다.")