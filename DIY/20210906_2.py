# 1
a = list(range(1, 11))
b = [n**2 for n in a]

dic = dict(zip(a, b))

print(dic[6])

# 2
price = [n*100 for n in range(1, 6)]
for i in map(lambda x:x*0.8, price):
    print(i)

# 3
score = [77, 88, 99, 66, 55]
score2 = score
score2[3] = 100
print(score[3])