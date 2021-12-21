# -*- coding: utf-8 -*-
import os
import chardet

close_expression = [".", "?", "!"]#종결표현
conversation_expression = ['\'', '\"']#대화문
exception_handling = ["..", "...", "....", "─"]#예외처리
match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪', '』':'『'}#괄호묶음
encodes = ['utf-8', 'utf-16', 'cp949', 'ANSI', 'euc-kr']

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
        if s in ['(', '{', '[', '「', '<', '≪', '『']:
            arr.append(s)#리스트에 추가
        elif s in [')', '}', ']', '」', '>', '≫', '』']:
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
        if s in ['(', '{', '[', '「', '<', '≪', '『']:#지금 문자가 여는 괄호인 경우
            temp_dict.setdefault(index)#딕셔너리 키값(여는 괄호 위치)에 추가
            temp.append(index)
            arr.append(s)
        elif s in [')', '}', ']', '」', '>', '≫', '』']:#지금 문자가 닫는 괄호인 경우
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

# def Line_Break_Handling(string):
#     if Parenthesis_Match_Check(string) == True:#괄호가 있을 경우
#         StartEndIndex = list(Parenthesis_Index_Check(string).items())
#         part = []
#         x = Parenthesis_Index_Check(string)            
#         for i in range(len(StartEndIndex)):#괄호와 내부 문자열 저장
#             part.append(string[StartEndIndex[i][0]:StartEndIndex[i][1]])
#         for i in range(len(part)):#괄호와 내부 문자열 제거
#             string = string.replace(part[i], "")
#         new_string = string
#         for i in range(len(part)):#괄호와 내부 문자열 후미로 이동
#             new_string = new_string + part[i]
#     elif Parenthesis_Match_Check(string) == None:#괄호가 없을 경우
#         pass
#     elif Parenthesis_Match_Check == False:#괄호가 짝짝이일 경우
#         pass


def ReadFile(path, name):
    with open(path + '\\\\' + filename,'r') as f:
            line = f.readline()
    file_data = chardet.detect(line.encode())
    print(file_data['encoding'])

    for encode in encodes:
        if encode == file_data['encoding']:
            try:
                f = open(path + '\\\\' + name,'r', encoding=encode)
                g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w', encoding=encode)

                while True:
                    r = f.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
                    if not r: break
                    g.write(r.replace(". ", ".\n\n") and r.replace(".\"", ".\n\""))
                    # FindAll(target)

                f.close()
                g.close()
            except UnicodeError:
                pass
            #'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록
            except FileNotFoundError:#파일경로에 txt 파일이 없을 경우
                print("File Not Found")

path = input('txt파일경로(위치)? ')
filename = input('txt파일명? ')
filename = filename + ".txt"

ReadFile(path, filename)


#'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록
# . 다음에 기호가 올 경우, 무시
# . 다음에 기호가 아닐 경우, 개행
# " 다음에 기호가 아닐 경우 무시
# 기호나 글자 다음에 "가 올 경우 개행
#index = find("\"")
#utf-8일 때, 한글 코드 범위: AC00-D7AF

# C:\Users\jeony\OneDrive\바탕 화면\test text

# 파일의 인코딩을 확인해서 그 인코딩으로만 파일을 읽고 불러들이자!