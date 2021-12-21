# -*- coding: utf-8 -*-

import os

def TextFileRename(path):

    files = os.listdir(path)
    i = 1
    index = -1
    for f in files:
        fullpath = path + "//" + f
        try:
            if(f.find("[") != -1 and f.find("]") != -1):
                while True:
                    i = i + 1
                    index = f.find("]", index + 1)
                    if index == -1:
                        break
                if i >= 2:
                    continue
                name = f[0:-4]
                ext = f[-4:]
                part = name.split("]")
                newname = part[1].strip() + part[0].strip() + "]" + ext
                print(newname)
                os.rename(path + "//" + f, path + "//" + newname)

            elif(f.find("(") != -1 and f.find(")") != -1):
                while True:
                    i = i + 1
                    index = f.find(")", index + 1)
                    if index == -1:
                        break
                if i >= 2:
                    continue
                name = f[0:-4]
                ext = f[-4:]
                part = name.split(")")
                newname = part[1].strip() + part[0].strip() + ")" + ext
                print(newname)
                os.rename(path + "//" + f, path + "//" + newname)
            
            # elif(f.find("+") != -1):
            #     while True:
            #         i = i + 1
            #         index = f.find("+", index + 1)
            #         if index == -1:
            #             break
            #     if i >= 2:
            #         continue
            #     name = f[0:-4]
            #     ext = f[-4:]
            #     part = name.split("+")
            #     newname = part[1].strip() + part[0].strip() + ext
            #     print(newname)
            #     os.rename(path + "//" + f, path + "//" + newname)

            if os.path.isdir(fullpath):
                TextFileRename(fullpath)
                
        except FileExistsError:
            continue

path = input('파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

TextFileRename(path)

# C:\Users\jeony\OneDrive\바탕 화면\test text