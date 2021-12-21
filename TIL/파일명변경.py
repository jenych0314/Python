import os

def Java_rename(file_path):
    lst = os.listdir(file_path)

    for obj in lst:
        if obj[3] == '장':
            l = list(obj)
            l[3] = '.'
            s = ''.join(l)
        else:
            s = obj
        first = s[:3]
        last = s[3:].replace('-', ' ')
        name = first + last
        print(name)
        file_oldname = os.path.join(file_path, obj)
        file_newname = os.path.join(file_path, name)
        os.rename(file_oldname, file_newname)

def IED_rename(file_path):
    lst = os.listdir(file_path)

    for obj in lst:
        first = obj[:7]
        mid = obj[7:9]
        last = obj[9:].replace('_', ' ')
        if first.startswith('SW_IED'):
            first = ''
        if mid.isnumeric():
            mid = int(mid)
            mid += 1
            mid = str(mid) + '.'
        name = first + str(mid) + last
        print(name)
        file_oldname = os.path.join(file_path, obj)
        file_newname = os.path.join(file_path, name)
        os.rename(file_oldname, file_newname)

def Psychology_rename(file_path):
    lst = os.listdir(file_path)

    for obj in lst:
        first = obj[:5]
        if first.startswith('마음과행동'):
            first = ''
        mid = obj[5:10].strip().replace('강', '. ')
        last = obj[10:]
        name = first + mid + last
        print(name)
        file_oldname = os.path.join(file_path, obj)
        file_newname = os.path.join(file_path, name)
        os.rename(file_oldname, file_newname)

file_path = input()
# IED_rename(file_path)
# Java_rename(file_path)
Psychology_rename(file_path)