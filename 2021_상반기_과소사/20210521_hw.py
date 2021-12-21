path = '.\\test text'
fname = 'vocabulary.txt'

dic = {}

with open(path + '\\\\' + fname, 'r') as f:
    while True:
        line = f.readline().split()
        if not line: break
        
        if len(line) == 6:
            dic[line[1]] = line[2]
            dic[line[4]] = line[5]
        else:
            index = []
            for i in range(len(line)):
                if line[i].isnumeric() == True:
                    index.append(i)

            meaning = [''.join(line[index[0]+2:index[1]]), ''.join(line[index[1]+2:])]
            dic[line[index[0]+1]] = meaning[0]
            dic[line[index[1]+1]] = meaning[1]
    
print(dic)

user_input = input('Please enter the English word: ')

if user_input in dic:
    print(dic[user_input])
else:
    print('Try Again')