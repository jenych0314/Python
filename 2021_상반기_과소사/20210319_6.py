import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()
print(now)

#오전 구분
if now.hour < 12:
    print('now is a.m.')
else:
    print('now is p.m.')