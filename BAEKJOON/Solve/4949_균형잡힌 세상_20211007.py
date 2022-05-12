import sys

match_parenthesis = {
    ')': '(', '}': '{', ']': '[', '」': '「', '>': '<', '≫': '≪'}


def Parenthesis_Match_Check(stirng):
    arr = []
    for s in stirng:
        # 지금 문자가 여는 괄호인 경우
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':
            arr.append(s)  # 리스트에 추가
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':  # 지금 문자가 닫는 괄호인 경우
            # 채워진 여는 괄호가 없거나 짝이 안 맞을 경우
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:
                return False  # 거짓 반환
            arr.pop()  # 짝이 맞을 경우 제거
    if len(arr) != 0:  # 여는 괄호만 있을 경우
        return False  # 거짓 반환

    return True  # 참 반환


while(True):
    string = sys.stdin.readline()
    if string == '.\n':
        break
    print('yes') if Parenthesis_Match_Check(string) else print('no')
