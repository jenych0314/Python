# -*- coding: utf-8 -*-

import os

match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪'}

def Parenthesis_Match_Check(string):
    arr = []
    open_parenthesis = list(match_parenthesis.values())
    close_parenthesis = list(match_parenthesis.keys())

    for i in string:
        if i in open_parenthesis or i in close_parenthesis:#어떤 괄호라도 있을 경우
            exsist = 1
            break
        else:#괄호가 없을 경우
            exsist = 0
    
    if exsist == 0:#괄호가 없을 경우
        return None

    for s in string:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':#지금 문자가 여는 괄호인 경우
            arr.append(s)#리스트에 추가
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':#지금 문자가 닫는 괄호인 경우
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False#거짓 반환
            arr.pop()#짝이 맞을 경우 제거

    if len(arr) != 0:#여는 괄호만 있을 경우
        return False#거짓 반환
    
    return True#참 반환

def Parenthesis_Index_Check(string):
    index = 0
    arr = []
    temp = []
    temp_dict = {}

    for s in string:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':#지금 문자가 여는 괄호인 경우
            temp_dict.setdefault(index)#딕셔너리 키값(여는 괄호 위치)에 추가
            temp.append(index)
            arr.append(s)
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':#지금 문자가 닫는 괄호인 경우
            if arr[len(arr) - 1] == match_parenthesis[s]:#
                temp_dict[temp[len(temp) - 1]] = index + 1#딕셔너리 키값에 밸루값(닫는 괄호 위치) 추가
                temp.pop()
                arr.pop()
        index += 1#지금 문자가 몇번째 문자인지 카운트
        
    StartEnd = list(temp_dict.items())
    temp_start = StartEnd[0][0]
    temp_end = StartEnd[0][1]
    re_range = {}

    for i in range(len(temp_dict)):#괄호 내부에 다른 괄호가 있을 경우 제외
        if StartEnd[i][0] <= temp_start or StartEnd[i][1] >= temp_end:
            temp_start = StartEnd[i][0]
            temp_end = StartEnd[i][1]
            re_range.setdefault(StartEnd[i][0],StartEnd[i][1])

    return re_range#최종 괄호 위치를 딕셔너리로 반환

def TextFileRename(path):

    files = os.listdir(path)
    print(files)

    for f in files:
        try:
            fullpath = path + "//" + f
            name = f[:-4]
            ext = f[-4:]
            if ext.lower() == '.txt':#텍스트 파일인 경우에만 실행
                if "+" in name:#텍스트 파일에 +가 띄어쓰기를 대체한 경우
                    name = name.replace("+", " ")
                elif "_" in name:
                    name = name.replace("_", " ")

                if Parenthesis_Match_Check(name) == True:#괄호가 멀쩡히 여닫힌 경우에만
                    StartEnd = list(Parenthesis_Index_Check(name).items())
                    part = []
                    for i in range(len(StartEnd)):#괄호와 내부 문자열 저장
                        part.append(name[StartEnd[i][0]:StartEnd[i][1]])
                    for i in range(len(part)):#괄호와 내부 문자열 제거
                        name = name.replace(part[i], "")
                    new_name = name
                    for i in range(len(part)):#괄호와 내부 문자열 후미로 이동
                        new_name = new_name + part[i]
                    new_name = new_name + ext
                else:#그 외 나머지 경우
                    new_name = name + ext#변경없음

                print(new_name)
                os.rename(path + "//" + f, path + "//" + new_name)

            if os.path.isdir(fullpath):#폴더 내부에 추가적으로 폴더가 있을 경우
                TextFileRename(fullpath)
                
        except FileNotFoundError:
            print("오류가 발생했습니다")
            continue

path = input('파일경로(위치)를 입력해주세요: ')

TextFileRename(path)

# C:\Users\jeony\OneDrive\바탕 화면\test text