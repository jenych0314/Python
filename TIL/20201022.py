#-*- coding: cp949 -*-
filename = input("파일명? ")
filename_1 = filename + '.txt'
filename_2 = filename + '_수정후.txt'
try:
    f = open(filename_1,'r',encoding='cp949')
    g = open(filename_2,'w',encoding='cp949')

    while True:
        line = f.readline().encode().decode('cp949')

        if len(line) == 0: break

        g.write(line.replace(". ", ".\n\n"))
        #print(r)

    f.close()
    g.close()
except FileNotFoundError as e:
    #print("파일이 없습니다.")
    print(e)
except AttributeError:
    pass
finally:
    if not f.closed:
        f.close()
    if not g.closed:
        g.close()