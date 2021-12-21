import copy
#1
lst1 = [1,2,3]
lst2 = lst1

lst2[1] = 100
print(lst1)
print(lst2)
#2
lst1 = [1,2,3]
lst2 = lst1.copy()

lst2[1] = 100
print(lst1)
print(lst2)
#3
lst0 = ['a','b']
lst1 = [lst0,2,3]
lst2 = lst1.copy()

lst2[0][1] = 'c'
print(lst1)
print(lst2)
#4
lst0 = ['a','b']
lst1 = [lst0,2,3]
lst2 = copy.deepcopy(lst1)

lst2[0][1] = 'c'
print(lst1)
print(lst2)