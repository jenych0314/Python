# -*- coding: utf-8 -*-
import os

close_expression = [".", "?", "!"]#종결표현
exception_handling = ["..", "...", "....", "─"]#예외처리
match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪'}#괄호묶음

def Parenthesis_Match_Check(stirng):#괄호가 잘 열리고 닫혀있는 지 확인
    arr = []

    for s in stirng:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':
            arr.append(s)
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':#닫는 괄호가 있는데
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False
            arr.pop()

    if len(arr) != 0:#여는 괄호만 있을 경우
        return False

    return True

# def Line_Break_Handling():#줄바꿈처리
#     if Parenthesis_Match_Check(line) == Ture:#멀쩡하게 괄호가 닫힘
#         #줄바꿈, 괄호 안의 내용 변경X
#     pass

def ReadWriteFile(path, name):
    try:
        file_read = open(path + '\\\\' + name,'r',encoding='utf-8')
        file_write = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')

        while True:
            line = file_read.readline()#\n, \r, \r\n 기준으로 읽힘
            if not line: break
            # if Parenthesis_Handling(line) == True:
            #     file_write.write(line.strip())
            pass

        file_read.close()
        file_write.close()
    #'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록
    except FileNotFoundError:#파일을 찾지 못했을 경우
        print("파일명을 정확하게 입력해주세요.")

path = input('txt파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

name = input('txt파일명? ')
if name[-4:] != '.txt':
    name += '.txt'

ReadWriteFile(path, name)

# . 다음에 기호가 올 경우, 무시
# . 다음에 기호가 아닐 경우, 개행
# " 다음에 기호가 아닐 경우 무시
# 기호나 글자 다음에 "가 올 경우 개행
#index = find("\"")
#utf-8일 때, 한글 코드 범위: AC00-D7AF

# C:\Users\jeony\OneDrive\바탕 화면\test text
