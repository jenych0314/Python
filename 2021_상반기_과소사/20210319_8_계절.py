import datetime

now = datetime.datetime.now()

if now.month == 3 or now.month == 4 or now.month == 5:
    print('spring')
elif now.month == 6 or now.month == 7 or now.month == 8:
    print('summer')
elif now.month == 9 or now.month == 10 or now.month == 11:
    print('fall')
else:
    print('winter')

# if 3 <= now.month <= 5:
#     print('spring')
# elif 6 <= now.month <= 8:
#     print('summer')
# elif 9 <= now.month <= 11:
#     print('fall')
# else:
#     print('winter')

# if now.month == 12 or now.month <= 2:
#     print('winter')
# elif now.month <= 5:
#     print('spring')
# elif now.month <= 8:
#     print('summer')
# else:
#     print('fall')

# if now.month in [12, 1, 2]:
#     print('winter')
# elif now.month <= 5:
#     print('spring')
# elif now.month <= 8:
#     print('summer')
# else:
#     print('fall')