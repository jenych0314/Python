arr = [chr(num) for num in range(106,96,-1)]

arrCopy = arr[:]
arrCopy.sort()

arrSorted = sorted(arr)

print(arr)
print(arrCopy)
print(arrSorted)