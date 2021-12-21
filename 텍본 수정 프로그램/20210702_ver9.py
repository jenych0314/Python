import chardet

encodes = ['utf-8', 'utf-16', 'cp949', 'ANSI', 'euc-kr']
conversation_expression = ["\'", "\""]#대화문
close_expression = [".", "?", "!"]#종결표현
exception_handling = ["..", "...", "....", "─"]#예외처리
parenthesis = {")":"(", "}":"{", "]":"[", "」":"「", ">":"<", "≫":"≪", "』":"『"}#괄호묶음
open_parenthesis = parenthesis.values()
close_parenthesis = parenthesis.keys()

def ParenthesisMatchCheck(string):
    stack = []

    for s in string:
        if s in open_parenthesis:
            stack.append(s)#여는 괄호 arr에 추가
        elif s in close_parenthesis:
            if (not stack) or (stack[-1] != parenthesis[s]):#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False
            stack.pop()#짝이 맞을 경우 제거

    return False if stack else True

def ParenthesisIdxCheck(string):
    IdxDict = {}
    stack = []
    
    for i in range(len(string)):
        if string[i] in open_parenthesis:#지금 문자가 여는 괄호인 경우
            IdxDict.setdefault(i)#딕셔너리 키값(여는 괄호 위치)에 추가
            stack.append([i, string[i]])
        elif string[i] in close_parenthesis:#지금 문자가 닫는 괄호인 경우
            if stack[-1][1] == parenthesis[string[i]]:
                IdxDict[stack[-1][0]] = i#딕셔너리 키값에 밸루값(닫는 괄호 위치) 추가
                stack.pop()
    
    return IdxDict

def ConversationMatchCheck(string):
    stack = []
    
    for s in string:
        if stack and (s in conversation_expression):
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        elif s in conversation_expression:
            stack.append(s)
    
    return False if stack else True

def IdxDictRerange(IdxDict):
    lst = list(IdxDict.items())
    StartIdx = lst[0][0]
    EndIdx = lst[0][1]
    RerangeDict = {}

    for i in range(len(IdxDict)):#내부에 같은 표현이 있을 경우 제외
        if lst[i][0] <= StartIdx or lst[i][1] >= EndIdx:
            StartIdx = lst[i][0]
            EndIdx = lst[i][1]
            RerangeDict.setdefault(lst[i][0], lst[i][1])

    return list(RerangeDict.items())#최종 위치를 이중리스트로 반환

def EncodingCheck(path, fname):
    try:
        f = open(path + '\\' + fname, 'r')
        file_data = f.readline()
        f.close()   
        return chardet.detect(file_data.encode())
    except UnicodeDecodeError:
        return None

def ModifyTextLine(string):
    string = string.strip() + '\n\n'

    for s in string:
        if (s in open_parenthesis) or (s in close_parenthesis):#어떤 괄호라도 있을 경우
            if ParenthesisMatchCheck(string) == True:#짝이 맞을 경우
                IdxLst = IdxDictRerange(ParenthesisIdxCheck(string))
                print(IdxLst)
                for i in range(len(IdxLst)):
                    pass
                break
            else:#짝이 맞지 않을 경우
                pass
        else:#괄호가 없을 경우
            break

    return string

path = input("path: ")
fname = input("file name: ")

if not 'txt' in fname:
    fname += '.txt'
    
Encode = EncodingCheck(path, fname)
for encode in encodes:
    try:
        f = open(path + '\\' + fname, 'r', encoding = encode)
        while True:
            line = f.readline()
            if not line: break
            string = ModifyTextLine(line)
        f.close()
        break
    except UnicodeDecodeError:
        print('can\'t decode the file with %s' %(encode))
    except UnicodeEncodeError:
        print('can\'t encode the file with %s' %(encode))
    except FileNotFoundError:
        print('can\'t find the file: %s' %(fname))