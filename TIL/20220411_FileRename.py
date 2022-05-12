import os

def twitter_media_file_rename(path):
    files = os.listdir(path)

    for f in files:
        ext = ['jfif']
        idx = f.rfind('.')
        if (f.find("-")) and f[idx:] in ext:
            name = f[:idx]
            ext = f[idx:]
            part = name.split("-")
            newname = part[1].strip() + "-" + part[0].strip() + ext
            os.rename(path + "//" + f, path + "//" + newname)

path = input('path: ')