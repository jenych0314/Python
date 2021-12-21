# -*- coding: utf-8 -*-

import os

match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪'}

def Parenthesis_Handling(string):
    arr = []
    TF = 0
    
    index = 0
    temp = []
    temp_dict = {}

    for s in string:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':#지금 문자가 여는 괄호인 경우
            arr.append(s)#리스트에 추가
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':#지금 문자가 닫는 괄호인 경우
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                TF = 0#거짓 반환
            arr.pop()#짝이 맞을 경우 제거

    if len(arr) != 0:#여는 괄호만 있을 경우
        TF = 0#거짓 반환

    TF = 1#참 반환

    if TF == 1:#참일 경우 괄호 위치 정보 읽어서 딕트로 변환
        _list = []

        for s in string:
            if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':
                temp_dict.setdefault(index)
                temp.append(index)
                _list.append(s)

            elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':
                if _list[len(_list) - 1] == match_parenthesis[s]:
                    temp_dict[temp[len(temp) - 1]] = index + 1
                    temp.pop()
                    _list.pop()

            index += 1

    start = list(temp_dict.keys())
    end = list(temp_dict.values())
    temp_start = start[0]
    temp_end = end[0]
    re_range = {}

    for i in range(len(temp_dict) - 1):#다른 괄호 내부에 있는 괄호 제거
        if start[i] <= temp_start or end[i] >= temp_end:
            temp_start = start[i]
            temp_end = end[i]
            re_range.setdefault(start[i],end[i])
    
    return re_range#괄호 위치 반환

def TextFileRename(path):

    files = os.listdir(path)

    for f in files:
        try:
            fullpath = path + "//" + f
            name = f[0:-4]
            ext = f[-4:]

            if ext.lower != '.txt':#txt파일이 아닌 경우
                continue#무시하고 다음 파일로 넘어가기

            part = Parenthesis_Handling(name)
            start = list(part.keys())

            # newname = name
            #part = name.split("")
            #newname = part[1].strip() + part[0].strip() + "" + ext
            # print(newname)
            # os.rename(path + "//" + f, path + "//" + newname)

            if os.path.isdir(fullpath):
                TextFileRename(fullpath)
                
        except:
            print("오류 발생\n")
            continue

while True:
    path = input('파일경로(위치)를 입력하세요: ')

    if path == '':
        print("현재 파일경로(위치)를 불러올까요? y/n")
        ans = input("->")

        if ans == 'y':
            # path = os.getcwd()#현 파일 위치 불러옴.
            try:
                TextFileRename(path)
            except FileNotFoundError:
                print("파일을 찾지 못했습니다")
            except:
                print("오류발생 종료합니다")
            break
        elif ans == 'n':
            continue
        else:
            print("종료합니다.")
            continue

    else:
        try:
            TextFileRename(path)
        except FileNotFoundError:
            print("파일을 찾지 못했습니다")
        except:
            print("오류발생 종료합니다")
        break

# C:\Users\jeony\OneDrive\바탕 화면\test text