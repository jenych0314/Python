t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1 - x2)**2 + (y1 - y2)**2
    # print('d',d)
    max_d = (r1 + r2)**2
    # print('max_d',max_d)
    min_d = (r1 - r2)**2
    # print('min_d',min_d)

    if (d == 0) and (r1 == r2):#case:-1
        print('-1')
    elif (d == max_d) or (d == min_d):#case:1
        print('1')
    elif min_d < d < max_d:#case:2
        print('2')
    else:#(d > max_d) or (d < min_d):#case:0
        print('0')