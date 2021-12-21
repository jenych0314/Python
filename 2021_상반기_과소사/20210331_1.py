import math
from time import time

n = 10123456879112837
start_time = time()

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print('not p')
        break
    else:
        # print('p')
        continue

print(time() - start_time)