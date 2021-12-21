#최빈값 찾기
lst = [1,2,3,4,4,4,5,5,6,6,6]
temp = set(lst)
dic = {}
result = []

if (len(temp) == 1) or (len(lst) == len(temp)):
    print('None')
else:
    for i in temp:
        dic[i] = lst.count(i)

    for j in dic:
        if dic[j] == max(dic.values()):
            result.append(j)

    print(result)