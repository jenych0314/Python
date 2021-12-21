match_parenthesis = {')':'(', '}':'{', ']':'[', '」':'「', '>':'<', '≫':'≪'}

def parenthesis_handling(stirng):
    arr = []
    for s in stirng:
        if s == '(' or s == '{' or s == '[' or s == '「' or s == '<' or s == '≪':
            arr.append(s)
        elif s == ')' or s == '}' or s == ']' or s == '」' or s == '>' or s == '≫':
            if len(arr) == 0 or arr[len(arr) - 1] != match_parenthesis[s]:
                return "False"
            arr.pop()
    if len(arr) != 0:
        return "False"
    
    return "True"

for t in range(int(input())):
    print('#{} {}'.format(t+1, parenthesis_handling(input())))