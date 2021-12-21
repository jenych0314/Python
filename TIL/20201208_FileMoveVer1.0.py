import os
import shutil

src = "C:\MUSIC"
dir = "C:\MUSIC\yet"

files = os.listdir(src)

for f in files:
    if f.find("-") == -1:
        filename = f
        shutil.move(src + "\\" + filename, dir + "\\" + filename)

# filename = "3 (Ft. Tall).mp3"