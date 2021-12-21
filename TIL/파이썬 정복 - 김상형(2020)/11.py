#1
a = list(range(1, 11))
b = [n**2 for n in a]

dic = dict(zip(a, b))
print(dic[6])

#2
price = [10, 20, 30, 40, 50]
for s in map(lambda x:x*0.8, price):
    print(s)