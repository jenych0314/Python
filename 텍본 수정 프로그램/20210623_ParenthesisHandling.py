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

def IdxDictRerange(IdxDict):
    lst = list(IdxDict.items())
    StartIdx = lst[0][0]
    EndIdx = lst[0][1]
    RerangeDict = {}

    for i in range(len(IdxDict)):#괄호 내부에 다른 괄호가 있을 경우 제외
        if lst[i][0] <= StartIdx or lst[i][1] >= EndIdx:
            StartIdx = lst[i][0]
            EndIdx = lst[i][1]
            RerangeDict.setdefault(lst[i][0], lst[i][1])

    return RerangeDict#최종 괄호 위치를 딕셔너리로 반환

string = """(()()()()[]()""[][][][][][][])"""


for s in string:
    if (s in open_parenthesis) or (s in close_parenthesis):#어떤 괄호라도 있을 경우
        if ParenthesisMatchCheck(string) == True:
            print(IdxDictRerange(ParenthesisIdxCheck(string)))
            break
    else:
        break