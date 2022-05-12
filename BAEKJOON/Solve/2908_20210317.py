a, b = map(str,input().split())
temp_a = ''
temp_b = ''

for i in range(3):
    temp_a += a[-(i + 1)]
    temp_b += b[-(i + 1)]

if int(temp_a) > int(temp_b):
    print(temp_a)
else:
    print(temp_b)