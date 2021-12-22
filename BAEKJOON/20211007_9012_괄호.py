import sys


def Parenthesis_Match_Check(string):
    arr = []
    for s in string:
        if s == '(':  # 지금 문자가 여는 괄호인 경우
            arr.append(s)  # 리스트에 추가
        elif s == ')':  # 지금 문자가 닫는 괄호인 경우
            if len(arr) == 0 or arr[-1] != '(':  # 채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False  # 거짓 반환
            arr.pop()  # 짝이 맞을 경우 제거
    if len(arr) != 0:  # 여는 괄호만 있을 경우
        return False  # 거짓 반환

    return True  # 참 반환


T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline()
    print('YES') if Parenthesis_Match_Check(string) else print('NO')
