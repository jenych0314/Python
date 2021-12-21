def solution(string):
    if len(string)%2 != 0:
        return 0

    stack = []
 
    for s in string:
        if s not in stack:
            stack.append(s)
        else:
            top = stack.pop()
            if top != s:
                stack.append(top)
                stack.append(s)
    
    if len(stack) == 0:
        return 1
    else:
        return 0

strings = ['cvccvccvccccvccc']

for string in strings:
    print(solution(string))