year = int(input())

if year % 400 == 0:
    print('T, a leap year')
elif year % 100 == 0:
    print('F, not a leap year')
elif year % 4 == 0:
    print('T, a leap year')
else:
    print('F, not a leap year')

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print('T, a leap year')
# else:
#     print('F, not a leap year')