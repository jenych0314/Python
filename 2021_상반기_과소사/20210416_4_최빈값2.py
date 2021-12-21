#최빈값 찾기
# lst = [1,2,3,4,4,4,5,5,6,6,6]
# lst = [1,1,1,1]
lst = [1,2,3]
temp = set(lst)
result = []

if not ((len(temp) == 1) or (len(lst) == len(temp))):
    dic = {i:lst.count(i) for i in temp}
    
    for key, value in dic.items():
        if value == max(dic.values()):
            result.append(key)

    print(result)