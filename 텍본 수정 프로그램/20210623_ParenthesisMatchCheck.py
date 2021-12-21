parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪', '』':'『'}#괄호묶음
open_parenthesis = parenthesis.values()
close_parenthesis = parenthesis.keys()

def ParenthesisMatchCheck(string):
    arr = []

    for s in string:
        if s in open_parenthesis:
            arr.append(s)#여는 괄호 arr에 추가
        elif s in close_parenthesis:
            if len(arr) == 0 or arr[len(arr) - 1] != parenthesis[s]:#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False
            arr.pop()#짝이 맞을 경우 제거

    if len(arr) != 0:#여는 괄호만 있을 경우
        return False
    
    return True

string = """()()()()[]()""[][][][][][][]"""

for s in string:
    if (s in open_parenthesis) or (s in close_parenthesis):#어떤 괄호라도 있을 경우
        print(ParenthesisMatchCheck(string))
        break
    else:
        break
