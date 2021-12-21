def readFile(self, path):

    lines = None
    try:
        ftype = 'normal'
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
    except:
        try:
            ftype = 'utf-8'
            f = open(path,'r',encoding='utf-8')
            lines = f.readlines()
            f.close()
        except:
            try:
                ftype = 'ANSI'
                f = open(path,'r',encoding='ANSI')
                lines = f.readlines()
                f.close()
            except:
                try:
                    ftype = 'utf-16'
                    f = open(path,'r',encoding='utf-16')
                    lines = f.readlines()
                    f.close()
                except:
                    print('file 읽기 실패', path)
                    return(False, ftype)

    for line in lines:
        sline = line.strip()

    return (True, ftype)

readFile('C:\\Users\\Owner\\Desktop\\사직 - 치욕의 특강.txt')