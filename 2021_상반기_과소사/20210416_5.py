# lst = [1,2,3,4,5,6,7,8,9,10,0,-1,-2]
# lst = [1,2,3]
# lst = [3,2,1]
lst = [1,1,1]
# print(lst == sorted(lst) or lst == sorted(lst, reverse=True))

ascending = True

for i in range(len(lst) - 1):
    if lst[i] == lst[i+1]:
        continue
    ascending = lst[i] < lst[i+1]
    break

for j in range(i+1, len(lst) - 1):
    if (ascending == True and lst[j] < lst[j+1]) or (not(ascending) and lst[j] > lst[j+1]) or (lst[j] == lst[j+1]):
        continue
    print(False)
    break
else:
    print(True)