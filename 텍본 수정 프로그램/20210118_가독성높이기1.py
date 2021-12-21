# -*- coding: utf-8 -*-
import os

# global.enter = "\n"
def ReadFile(path, name):
    f = open(path + '\\\\' + name,'r',encoding='utf-8')
    g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')

    while True:
        r = f.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
        if not r: break
        # r.splitlines()
        index = -1
        target = '.'
        _list = []
        while True:
            index = r.find(target, index + 1)
            if index == -1:
                break
        # .을 모두 검색
            _list.append(index)#리스트에 전부 추가
            # print('start = %d' %index)
        # print(_list)
        for n in range(0, len(_list) - 1):# .이 연달아 있는지 검사
            if _list[n+1] == _list[n] + 1:
                # print("ok")
                g.write(r)
            else:
                g.write(r.replace(".", ".\n\n"))        

    f.close()
    g.close()
    #'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록

path = input('path? ')

name = input('txt파일명? ')
if name[-4:] != '.txt':
    name += '.txt'

ReadFile(path, name)

# . 다음에 기호가 올 경우, 무시
# . 다음에 기호가 아닐 경우, 개행
# " 다음에 기호가 아닐 경우 무시
# 기호나 글자 다음에 "가 올 경우 개행
#index = find("\"")
#utf-8일 때, 한글 코드 범위: AC00-D7AF