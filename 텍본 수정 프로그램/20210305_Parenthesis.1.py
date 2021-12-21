match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪'}
index = 0
temp = []
temp_dict = {}

def Parenthesis_Match_Check(stirng):
    arr = []
    for s in stirng:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':#지금 문자가 여는 괄호인 경우
            arr.append(s)#리스트에 추가
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':#지금 문자가 닫는 괄호인 경우
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:#채워진 여는 괄호가 없거나 짝이 안 맞을 경우
                return False#거짓 반환
            arr.pop()#짝이 맞을 경우 제거
    if len(arr) != 0:#여는 괄호만 있을 경우
        return False#거짓 반환
    
    return True#참 반환

string = input()

if Parenthesis_Match_Check(string) == True:#참인 경우 괄호 위치를 저장해 딕트로 다시 만듦
    _list = []
    for s in string:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':
            temp_dict.setdefault(index)
            temp.append(index)
            _list.append(s)
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':
            if _list[len(_list) - 1] == match_parenthesis[s]:
                temp_dict[temp[len(temp) - 1]] = index + 1
                temp.pop()
                _list.pop()
        index += 1

print(temp_dict)

start = list(temp_dict.keys())
end = list(temp_dict.values())
temp_start = start[0]
temp_end = end[0]
re_range = {}

for i in range(len(temp_dict) - 1):
    if start[i] <= temp_start or end[i] >= temp_end:
        temp_start = start[i]
        temp_end = end[i]
        re_range.setdefault(start[i],end[i])

print(re_range)

#[( <   > ) ] ( { })