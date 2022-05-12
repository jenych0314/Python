# -*- coding: utf-8 -*-

import os


def python_file_name_change(path):
    files = os.listdir(path)

    for file in files:
        try:
            file = file[:-3]
            name = file.split('_')
            if len(name) == 2:
                newname = '_'.join(name[::-1]) + '.py'
            elif len(name) == 3:
                newname = f'{name[1]}_{name[2]}_{name[0]}.py'
            print(newname)
            os.rename(path + "\\" + file, path + "\\" + newname)

            # fullpath = path + "//" + file
            # if os.path.isdir(fullpath):
            #     python_file_name_change(fullpath)
        except FileExistsError:
            continue
        except FileNotFoundError as e:
            continue


path = input('파일경로(위치)? ')
if path == '':
    path = os.getcwd()  # 현 파일 위치 불러옴.

python_file_name_change(path)
