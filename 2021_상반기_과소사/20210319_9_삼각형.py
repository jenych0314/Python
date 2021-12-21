print('<Check the triangle.>')

a, b, c = map(int, input('Enter three positive numbers that are divided into spaces.\n->').split())

if a == max(a, b, c):
    big = a
    rest = [b, c]
elif b == max(a, b, c):
    big = b
    rest = [a, c]
else:
    big = c
    rest = [a, b]

if big < sum(rest):
    print('Triangle can exsist.')
    if big ** 2 == rest[0] ** 2 + rest[1] ** 2:
        print('∆abc is a right triangle')
    elif big ** 2 < rest[0] ** 2 + rest[1] ** 2:
        print('∆abc is an acute triangle')
    else:
        print('∆abc is an obtuse triangle')
else:
    print('Triangle can\'t exsist.')

# if a == max(a, b, c):
#     if a < b + c:
#         print('Triangle can exsist.')
#         if a ** 2 == b ** 2 + c ** 2:
#             print('∆abc is a right triangle')
#         elif a ** 2 < b ** 2 + c ** 2:
#             print('∆abc is an acute triangle')
#         else:
#             print('∆abc is an obtuse triangle')
#     else:
#         print('Triangle can\'t exsist.')
# elif b == max(a, b, c):
#     if b < a + c:
#         print('Triangle can exsist.')
#         if b ** 2 == a ** 2 + c ** 2:
#             print('∆abc is a right triangle')
#         elif b ** 2 < a ** 2 + c ** 2:
#             print('∆abc is an acute triangle')
#         else:
#             print('∆abc is an obtuse triangle')
#     else:
#         print('Triangle can\'t exsist.')
# else:
#     if c < a + b:
#         print('Triangle can exsist.')
#         if c ** 2 == a ** 2 + b ** 2:
#             print('∆abc is a right triangle')
#         elif c ** 2 < a ** 2 + b ** 2:
#             print('∆abc is an acute triangle')
#         else:
#             print('∆abc is an obtuse triangle')
#     else:
#         print('Triangle can\'t exsist.')