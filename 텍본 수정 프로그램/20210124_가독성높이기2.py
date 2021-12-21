# -*- coding: utf-8 -*-

#C:\Users\jeony\OneDrive\바탕 화면\test text

import os
AllString = []
def ReadFile(path, name):
    index1 = -1; index2 = -1
    target1 = "「"; target2 = "」"
    list1 = []; list2 = []
    
    try:
        fr = open(path + '\\\\' + name,'r',encoding='utf-8')
        fw = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')

        while True:
            string = fr.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
            AllString.append(string)
            if not string: 
                # list(filter(None, string))
                break#빈 줄
        
            while True:
                # index1 = string.find(target1, index1 + 1)
                index2 = string.find(target2, index2 + 1)
                if index2 == -1:
                    break
                # list1.append(index1)
                # list2.append(index2)
                # for n in range(0, len(list1) - 1):
                #     if list1[n] + 1 == list1[n+1]: #...
                #         pass
                #     else:
                #         pass
            
            fw.write(string.replace("「", "\n\n「"))

            # print(list1)
            # print(list2)

        fr.close()
        fw.close()
    #'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록
    
    except FileNotFoundError:#파일경로에 txt 파일이 없을 경우
        print("파일명을 정확하게 입력해주세요.")

path = input('txt파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

name = input('txt파일명? ')
if name[-4:] != '.txt':
    name += '.txt'
    
print(AllString)
ReadFile(path, name)