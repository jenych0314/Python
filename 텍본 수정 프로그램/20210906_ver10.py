# -*- coding: utf-8 -*-

_encodings = ['utf-8', 'cp949', 'euc-kr']
quatation_marks = ['\'', '\"']
close_expression = ['.', '?', '!']
special_character = '~!@#$%^&*-=_+./:;|\\|'
parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪', '』':'『'}#괄호묶음
open_parenthesis = parenthesis.values()
close_parenthesis = parenthesis.keys()

def quatation_idx_check(string):
    stack = []
    idx_dict = {}

    for i in range(len(string)):
        if stack and (string[i] in quatation_marks):
            if stack[-1][1] == string[i]:
                idx_dict[stack[-1][0]] = i
                stack.pop()
            else:
                stack.append([i, string[i]])
                idx_dict.setdefault(i)
        elif string[i] in quatation_marks:
            stack.append([i, string[i]])
            idx_dict.setdefault(i)
    
    return [] if stack else list(idx_dict.items())

def parenthesis_idx_check(string):
    stack = []
    idx_dict = {}

    for i in range(len(string)):
        if string[i] in open_parenthesis:
            idx_dict.setdefault(i)
            stack.append([i, string[i]])#여는 괄호 arr에 추가
        elif string[i] in close_parenthesis:
            if (not stack) or (stack[-1][1] != parenthesis[string[i]]):#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return []
            else:
                idx_dict[stack[-1][0]] = i
                stack.pop()#짝이 맞을 경우 제거

    return [] if stack else list(idx_dict.items())

def close_expression_idx_check(string):
    idx_dict = {}
    temp = []

    for i in range(len(string)):
        if string[i] in close_expression:
            idx_dict[i] = i
            temp.append(i)
            for j in range(len(string) - i):
                if any(s in string[i+j] for s in special_character) or (string[i+j] in close_expression):
                    idx_dict[i] = i+j
                else:
                    break
    return list(idx_dict.items())

def idx_rerange(idx_lst):
    start = idx_lst[0][0]
    last = idx_lst[0][1]
    reranged_dict = {}

    for i in range(len(idx_lst)):#내부에 같은 표현이 있을 경우 제외
        if idx_lst[i][0] <= start or idx_lst[i][1] > last:
            start = idx_lst[i][0]
            last = idx_lst[i][1]
            reranged_dict.setdefault(idx_lst[i][0], idx_lst[i][1])

    return list(reranged_dict.items())#최종 위치를 이중리스트로 반환

def clear_string(string):
    quatation_exsist = False
    parenthesis_exsist = False
    close_expression_exsist = False
    
    for i in range(len(string)):
        if string[i] in quatation_marks:
            quatation_exsist = True
        elif (string[i] in open_parenthesis) or (string[i] in close_parenthesis):
            parenthesis_exsist = True
        elif string[i] in close_expression:
            close_expression_exsist = True

    idx_lst = []
    quatation_idx = []
    parenthesis_idx = []
    close_expression_idx = []
    reranged_idx = []
    
    if quatation_exsist == True:
        quatation_idx = quatation_idx_check(string)
    if parenthesis_exsist == True:
        parenthesis_idx = parenthesis_idx_check(string)
    if close_expression_exsist == True:
        close_expression_idx = close_expression_idx_check(string)
    
    idx_lst = quatation_idx + parenthesis_idx + close_expression_idx
    idx_lst.sort()
    
    if idx_lst:
        reranged_idx = idx_rerange(idx_lst)

    for i in range(len(reranged_idx)):
        if reranged_idx[i][0] == reranged_idx[i][1]:
            string = string[:reranged_idx[i][0]+1] + '\n\n' + string[reranged_idx[i][0]+1:]
        else:
            string = string[:reranged_idx[i][0]+1] + '\n\n' + string[reranged_idx[i][0]+1:reranged_idx[i][1]+1] + '\n\n' + string[reranged_idx[i][1]+1:]
    
    return string

file_path = input('file path?: ')
file_name = input('file name?: ')

if not 'txt' in file_name:
    file_name += '.txt'

for _encode in _encodings:
    try:
        file_read = open(file_path + '\\' + file_name, 'r', encoding= _encode)
        file_write = open(file_path + '\\' + 'Modified ' + file_name, 'w', encoding= _encode)
        while True:
            line = file_read.readline()
            if not line: break # 마지막 줄일 경우 종료
            elif not line.strip(): continue # 개행문자로 이뤄진 빈줄 없앰
            line = clear_string(line)
            file_write.write(line)

        file_read.close()
        file_write.close()
        break
    except UnicodeDecodeError:
        print('can\'t decode the file with %s' %(_encode))
    except UnicodeEncodeError:
        print('can\'t encode the file with %s' %(_encode))
    except FileNotFoundError:
        print('can\'t find the file: %s' %(file_name))