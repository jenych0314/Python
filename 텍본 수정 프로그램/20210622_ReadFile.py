import chardet

encodes = ['utf-8', 'utf-16', 'cp949', 'ANSI', 'euc-kr']

def EncodingCheck(path, fname):
    try:
        f = open(path + '\\' + fname, 'r')
        file_data = f.readline()
        return chardet.detect(file_data.encode())
    except UnicodeDecodeError:
        return None
    finally:
        f.close()   

def ReadFile(path, fname):
    Encoding = EncodingCheck(path, fname)
    if Encoding != None:
        with open(path + '\\' + fname, 'r', encoding = Encoding) as f:
            pass
    else:
        for encode in encodes:
            try:
                f = open(path + '\\' + fname, 'r', encoding = encode)
            except UnicodeDecodeError:
                print('can\'t read the file with %s' %(encode))
                continue
            finally:
                f.close()
                break

path = input()
fname = input()

ReadFile(path, fname)