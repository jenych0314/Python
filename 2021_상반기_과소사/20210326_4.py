import time
n = int(input('자연수: '))

start_time = time.time()

for i in range(2, n):
    if n % i == 0:
        print('not p')
        break
else:
    print('p')

print(time.time() - start_time)