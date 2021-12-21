# cabinet = {3:"유재석", 4:"조세호", 1010:"김태호"}
# print(cabinet[3])
# print(cabinet[5])
# print(cabinet.get(4))
# print(cabinet.get(5,"주후니"))
# print(3 in cabinet) #True
# cabinet = {"a-3":"유재석", "b-4":"조세호", "c+1010":"김태호"}
# print(cabinet.keys())# only key
# print(cabinet.values())# only value
# print(cabinet.items())#pair key and value
# menu = ("돈까스","치즈까스") #튜플
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("유재석")
print(java)