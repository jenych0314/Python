# -*- coding: utf-8 -*-

#C:\Users\jeony\OneDrive\바탕 화면\test text

import os

AllString = []

def ReadFile(path, name):
    global AllString
    fr = open(path + '\\\\' + name,'r',encoding='utf-8')

    while True:
        string = fr.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
        if not string: break#빈 줄
        AllString.append(string)
        # fw.write(string.replace("", ""))
       
    AllString = list(filter(None, AllString))
    # set(AllString)
    # list(AllString)
        
    fr.close()

def WriteFile(path, name):
    global AllString
    fr = open(path + '\\\\' + name,'r',encoding='utf-8')
    fw = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')
       
    for n in range(0, (len(AllString) - 1)):
        fw.write(AllString[n])
        
    fr.close()
    fw.close()

# def CheckFile(path, name):

    index = -1
    target = [".", "'", "\"", "[", "]", "(", ")", "「","」"]
    flist = []

    try:
        fr = open(path + '\\\\' + name,'r',encoding='utf-8')
        fw = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')

        while True:
            string = fr.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
            if not string: break#빈 줄
        
        while True:
            for n in range(0, len(target) - 1):
                index = string.find(target[n], index + 1)
                if index == -1:
                    break
                flist.append(index)#리스트에 전부 추가
                fw.write(target[n])
                fw.write(flist)
            fw.write("\n")
        # for n in range(0, len(flist) - 1):# .이 연달아 있는지 검사
        #     if flist[n+1] == flist[n] + 1:

        fr.close()
        fw.close()
    
    except FileNotFoundError:
        print("파일명을 정확하게 입력해주세요.")

path = input('txt파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

name = input('txt파일명? ')
if name[-4:] != '.txt':
    name += '.txt'
    
ReadFile(path, name)
WriteFile(path, name)
# CheckFile(path, name)

