n = int(input())
cnt = 0

for i in range(n):
    string = input()
    temp = []
    check_group = True
    for j in range(len(string)):
        temp.append(string[j])
        if (string[j] != temp[j - 1]) and (string[j] in temp[:j - 1]):
            check_group = False
    if check_group == True:
        cnt += 1
print(cnt)