balance = 10
year = 0
while balance < 20 and year < 10:
    balance *= 1.05
    year += 1
    # if year >= 10:
    #     break
    print('{}, {}'.format(year, balance))

print('total: {}, {}'.format(year, balance))