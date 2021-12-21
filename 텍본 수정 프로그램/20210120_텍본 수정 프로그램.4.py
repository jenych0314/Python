# -*- coding: utf-8 -*-
import os

def ReadFile(path, name):
    try:
        f = open(path + '\\\\' + name,'r',encoding='utf-8')
        g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-8')

        while True:
            r = f.readline()#한 줄씩 읽는데 엔터 기준으로 한 줄로 인식
            if not r: break
            g.write(r.replace(". ", ".\n\n") and r.replace(".\"",".\n\""))
            # FindAll(target)

        f.close()
        g.close()
    #'', "", [], (), 「」사이에 문장은 바꾸는 게 안되도록
    except UnicodeDecodeError:#파일이 utf-8로 읽혀지지 않아서 오류가 뜰 경우
        try:
            f = open(path + '\\\\' + name,'r',encoding='utf-16')
            g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='ANSI')

            while True:
                r = f.readline()
                if not r: break
                g.write(r.replace(". ", ".\n\n") and r.replace(".\"",".\n\""))
                # FindAll(target)

            f.close()
            g.close()
        except UnicodeDecodeError:#파일이 utf-16로 읽혀지지 않아서 오류가 뜰 경우
            try:
                f = open(path + '\\\\' + name,'r',encoding='cp949')
                g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-16')

                while True:
                    r = f.readline()
                    if not r: break
                    g.write(r.replace(". ", ".\n\n") and r.replace(".\"",".\n\""))
                    # FindAll(target)

                f.close()
                g.close()
            except UnicodeDecodeError:#파일이 ansi(cp949)으로 읽혀지지 않아서 오류가 뜰 경우
                try:
                    f = open(path + '\\\\' + name,'r',encoding='euc-kr')
                    g = open(path + '\\\\' + name[:-4] + '_수정후' + name[-4:],'w',encoding='utf-16')

                    while True:
                        r = f.readline()
                        if not r: break
                        g.write(r.replace(". ", ".\n\n") and r.replace(".\"",".\n\""))
                        # FindAll(target)

                    f.close()
                    g.close()
                except UnicodeDecodeError:#파일이 euc-kr으로 읽혀지지 않아서 오류가 뜰 경우
                    print("파일이 읽혀지지 않습니다.")
    except FileNotFoundError:#파일경로에 txt 파일이 없을 경우
        print("파일명을 정확하게 입력해주세요.")

# def FindAll(target):
    # index = -1
    # target = '.'
    # _list = []
    # while True:
        # index = .find(target, index + 1) # target을 모두 검색
        # if index == -1:
            # break
        # _list.append(index)#리스트에 전부 추가
            # print('start = %d' %index)
        # print(_list)
    # for n in range(0, len(_list) - 1):
    #     if _list[n] + 1 == _list[n+1]:# .이 연달아 있는지 검사
    #         print("ok")
    #         g.write(r)
    #     else:
    #         g.write(r.replace(".", ".\n\n"))

path = input('txt파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

name = input('txt파일명? ')
if name[-4:] != '.txt':
    name += '.txt'

# target = input(' ')
ReadFile(path, name)
# print(FindAll(target))
# . 다음에 기호가 올 경우, 무시
# . 다음에 기호가 아닐 경우, 개행
# " 다음에 기호가 아닐 경우 무시
# 기호나 글자 다음에 "가 올 경우 개행
#index = find("\"")
#utf-8일 때, 한글 코드 범위: AC00-D7AF