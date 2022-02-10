a, b, c = map(int, input().split())#a = 고정비용, b = 가변비용, c = 가격
x, cost, income = 0, 0, 0#판매량, 비용, 수입

if b >= c:
    print(-1)
else:
    x = int(-(a / (b-c)) + 1)
    print(x)