string = input()
cnt = 0

if len(string) > 1:
    for i in range(len(string)):
        if string[i] == 'c' and (i+1) < (len(string)):
            if string[i+1] in ['=', '-']:
                continue
            else:
                cnt += 1

        elif string[i] in ['l', 'n'] and (i+1) < (len(string)):
            if string[i+1] == 'j':
                continue
            else:
                cnt += 1

        elif string[i] in ['s', 'z'] and (i+1) < (len(string)):
            if string[i+1] == '=':
                continue
            else:
                cnt += 1

        elif string[i] == 'd' and (i+1) < (len(string)):
            if string[i+1] == '-':
                continue
            elif string[i+1] == 'z' and (i+2) < (len(string)):
                if string[i+2] == '=':
                    continue
                else:
                    cnt += 1
            else:
                cnt += 1

        else:
            cnt += 1
            
else:
    cnt = len(string)

print(cnt)