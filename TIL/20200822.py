import matplotlib.pyplot as plt
import pandas as pd

def readTxt_returnList(txtPath):
    fstream=open(txtPath,encoding="utf-8")
    rlist = fstream.readlines()
    fstream.close()
    return rlist

dataFilePath = "user/poketmon_data.txt"
indexFilePath = "user/poketmon_index.txt"

poketmon_name_list = list()

temp_list = readTxt_returnList(indexFilePath)
for i in temp_list:
    poketmon_name_list.append(i.strip())

poketmon_count_list=list()

for i in poketmon_name_list:
    poketmon_count_list.append(0)

print(len(poketmon_name_list))
print(len(poketmon_count_list))

all_poketmonData_list = readTxt_returnList(dataFilePath)

for each in all_poketmonData_list:
    each_poketmon = each.strip()
    target_index = poketmon_name_list.index(each_poketmon)
    poketmon_count_list[target_index] += 1

print(poketmon_name_list)
print(poketmon_count_list)

for i in range(len(poketmon_name_list)):
    print(poketmon_name_list[i], ":", poketmon_count_list[i])


plt.plot(poketmon_name_list,poketmon_count_list)
plt.bar(poketmon_name_list,poketmon_count_list,width=0.5,color="grey")
plt.title("Poketmon counter")
plt.xlabel("name")
plt.ylabel("num")
plt.show()