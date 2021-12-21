# -*- coding: utf-8 -*-

import os

def ExtChange(path,OldExt,NewExt):

    files = os.listdir(path)

    for f in files:
        fullpath = path + "//" + f
        try:
            if(f.endswith(OldExt)):
                name = f[:-(len(OldExt) + 1)]
                ext = f[-(len(OldExt)):]
                ext = NewExt
                newname = name + ext
                print(newname)
                os.rename(path + "//" + f, path + "//" + newname)

            if os.path.isdir(fullpath):
                ExtChange(fullpath, OldExt, NewExt)
        except FileExistsError:
            continue

path = input('파일경로(위치)? ')
if path == '':
    path = os.getcwd()#현 파일 위치 불러옴.

OldExt = input('Old 확장자? ')
if OldExt.find(".") == -1:
    OldExt = "." + OldExt

NewExt = input('New 확장자? ')
if NewExt.find(".") == -1:
    NewExt = "." + NewExt

ExtChange(path, OldExt, NewExt)