import sys
input = sys.stdin.readline


while(True):
    string = input().strip()
    if string == '0':
        break

    length = len(string)
    half_length = length // 2

    if length % 2 == 0:
        if string[:half_length] == string[-1:half_length-1:-1]:
            print('yes')
        else:
            print('no')
    else:
        if string[:half_length] == string[-1:half_length:-1]:
            print('yes')
        else:
            print('no')
