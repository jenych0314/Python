import os
import shutil

def music_file_rename(path):
    files = os.listdir(path)

    for f in files:
        ext = ['.mp3', '.flac', '.wav', '.DSD']
        idx = f.rfind('.')
        if (f.find("-")) and f[idx:] in ext:
            name = f[:idx]
            ext = f[idx:]
            part = name.split("-")
            newname = part[1].strip() + "-" + part[0].strip() + ext
            os.rename(path + "//" + f, path + "//" + newname)
        # if f.find("-") == -1:
        #     os.makedirs('./test')
        #     shutil.move(path, "./test")

path = input('path: ')
music_file_rename(path)