# 1. 입력으로 두 수 m,n(m>n)이 들어온다.
# 2. n이 0이라면, m을 출력하고 알고리즘을 종료한다.
# 3. m이 n으로 나누어 떨어지면, n을 출력하고 알고리즘을 종료한다.
# 4. 그렇지 않으면, m을 n으로 나눈 나머지를 새롭게 n에 대입하고, m과 n을 바꾸고 3번으로 돌아온다.

m, n = map(int, input().split())

while n != 0:
    m, n = n, m%n
else:
    print('최대 공약수: {}'.format(m))

# if m % n == 0:
#     print('최대 공약수 {}'.format(n))
# else:
#     m, n = n, m%n


#     if m%n == 0:
#         print('최대 공약수 {}'.format(n))
#     else:
#         m, n = n, m%n
#         if m%n == 0:
#             print('최대 공약수 {}'.format(n))
#         else:
#             m, n = n, m%n