import sys
input = sys.stdin.readline

def solve(string):
    
    stack = []
    for ch in string:

        if len(stack) == 0 and ch == ')':
            return "NO"
        
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return "NO"
    
    if len(stack) == 0:
        return "YES"
    return "NO"

if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        string = input().strip()
        print(solve(string))