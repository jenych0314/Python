xLst = []
yLst = []

for i in range(3):
    x, y = map(int, input().split())

    if x in xLst:
        xLst.remove(x)
    else:
        xLst.append(x)
    if y in yLst:
        yLst.remove(y)
    else:
        yLst.append(y)

print(xLst[0], yLst[0])