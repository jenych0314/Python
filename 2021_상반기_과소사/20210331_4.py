#지금 시간
#시간에 10초 더하기(종료 시간)
#반복
#반복조건: 지금 시간 < 종료 시간
#반복: 더하기
#변이 요소: 없음

#시간
#비교
#반복 결정
import time

n = 10
cnt = 0

target_time = time.time() + n

while time.time() < target_time:
    cnt += 1
else:
    print(cnt)