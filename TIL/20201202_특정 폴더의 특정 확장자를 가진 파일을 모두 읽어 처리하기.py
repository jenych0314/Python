import codecs
import os

class CFolderFile:
    def __init__(self):
        self.ftypelist = {}
    
    def FolderNavigate(self, path, extlst):
        for fname in os.listdir(path):
            fullname = os.path.join(path, fname)

            if os. path.isdir(fullname):
                self.FolderNavigate(fullname, extlst)
            else:
                llist = fullname.split('.')
                ext = llist[-1]
                ext.lower()

                if ext in extlst:
                    ret, ftype = self.readFile(fullname)
                    if not ftype in self.ftypelist:
                        self.ftypelist[ftype] = 1
                    else:
                        self.ftypelist[ftype] = self.ftypelist[ftype] + 1
        
        return True

def readFile(self, path):

    ftype = 'normal'
    f = open(path, 'r')
    lines = None
    try:
        lines = f.readlines()
    except:
        f.close()
        try:
            ftype = 'utf-8'
            f = codecs.open(path,'r','utf-8')
            lines = f.readlines()
        except:
            try:
                ftype = 'utf-16'
                f = codecs.open(path,'r','utf-16')
                lines = f.readlines()
            except:
                try:
                    ftype = 'ANSI'
                    f = codecs.open(path,'r','ANSI')
                    lines = f.readlines()
                except:
                    print('file 읽기 실패', path)
                    return(False, ftype)
    f.close()

    for line in lines:
        sline = line.strip()

    return (True, ftype)

Path = 'C:\Users\jeony\Downloads\media'
extlist = {'jfif'}
objFolder = CFolderFile()
objFolder.FolderNavigate(Path, extlist)