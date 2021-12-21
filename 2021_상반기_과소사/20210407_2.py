arr = list(range(1,6))
CopyArr = arr[:]
OcationArr = arr

print(CopyArr)
print(arr)
print(OcationArr)

CopyArr.append(6)
arr.append(7)

print(CopyArr)
print(arr)
print(OcationArr)