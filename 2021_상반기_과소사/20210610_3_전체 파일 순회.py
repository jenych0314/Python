import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "//" + f
        try:
            if os.path.isdir(fullpath):
                print("[" + fullpath + "]")
                dumpdir(fullpath)
            else:
                print("\t" + fullpath)
        except PermissionError:
            print("PermissionError")

f = open('dumpdir.txt', 'w')
f.write(dumpdir("C:/Users/jeony/OneDrive/"))
f.close()