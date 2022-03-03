match_dict = {'}':'{',')':'('}

def solution(user_input):
    arr = []
    for s in user_input:
        if s == '(' or s == '{':
            arr.append(s)
        elif s == ')' or s == '}':
            if len(arr) == 0 or arr[len(arr) - 1] != match_dict[s]:
                return "NO"
            arr.pop()
    if len(arr) != 0:
        return "NO"
    
    return "YES"

for t in range(int(input())):
    print('#{} {}'.format(t+1, solution(input())))