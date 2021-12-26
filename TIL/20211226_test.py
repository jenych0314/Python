lst = [i for i in range(10)]

for x in lst[:]:
    print(x)
    lst.remove(x)