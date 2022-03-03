import pickle

data_base = []
keyname = 'Name'

def read_db():
    global data_base
    with open(f'{file_name}', 'rb') as f:
        data_base = pickle.load(f)
        for data in data_base:
            data['Age'] = int(data['Age'])
            data['Score'] = int(data['Score'])
    return data_base

def write_db():
    global data_base
    with open(f'{file_name}', 'wb') as f:
        pickle.dump(data_base, f)

def add_db(name, age, score):
    global data_base

    try:
        if name.isalpha():
            name = name[0].upper() + name[1:].lower()
        else:
            raise ValueError
        record = {'Name':name, 'Age':int(age), 'Score':int(score)}
        data_base += [record]
        return data_base
    except ValueError:
        print('Enter the name: English, age: integer, score: integer')

def del_db(name):
    global data_base

    try:
        if name.isalpha():
            name = name[0].upper() + name[1:].lower()
        else:
            raise ValueError

        print(f'Do you want to delete {name}? yes/no')
        reply = input().lower().strip()
        if reply == 'yes':
            cnt = 0
            for p in data_base:
                if p['Name'] == name:
                    print('delete list')
                    for attr in sorted(p):
                        print(attr + ' = ' + str(p[attr]), end = ' ')
                    print()
                    data_base.remove(p)
                    cnt += 1
            
            if cnt == 0:
                print('There\'s no', name)

        return data_base
    except ValueError:
        print('Enter the name: English')

def show_db(keyname): #sortkey가 가장 왼쪽에 나오게끔 출력
    global data_base

    try:
        for p in sorted(data_base, key = lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + ' = ' + str(p[attr]), end = ', ')
            print()
    except KeyError:
        print('sortKeys: Name, Age, Score')

def find_db(name):
    global data_base

    try:
        if name.isalpha():
            name = name[0].upper() + name[1:].lower()
        else:
            raise ValueError
        cnt = 0

        for p in data_base:
            if p['Name'] == name:
                for attr in sorted(p):
                    print(attr + ' = ' + str(p[attr]), end = ' ')
                print()
                cnt += 1

        if cnt == 0:
            print('Cannot find', name)
    except ValueError:
        print('Enter the name: English')

def inc_db(name, amount):
    global data_base

    try:
        if name.isalpha():
            name = name[0].upper() + name[1:].lower()
        else:
            raise ValueError
        amount = int(amount)
        for p in data_base:
            if p['Name'] == name:
                p['Score'] += amount
        return data_base
    except ValueError:
        print('Enter the name: English, amount: integer')

def do_db():
    global data_base, keyname

    while True:
        try:
            input_str = input('DB > ')
        except KeyboardInterrupt:
            continue

        if input_str == '': continue

        parse = input_str.split(' ')
        commands = ['add', 'del', 'show', 'quit', 'find', 'inc']

        if parse[0] in commands:
            if parse[0] == commands[0]: # add
                try:
                    add_db(parse[1], parse[2], parse[3])
                except IndexError:
                    print('Type \'add name age score\'')

            elif parse[0] == commands[1]: # del
                name = input('Enter the name: ') if len(parse) == 1 else parse[1]
                del_db(name)

            elif parse[0] == commands[2]: # show
                try:
                    if len(parse) == 1:
                        show_db(keyname)
                    else:
                        sortKey = parse[1][0].upper() + parse[1][1:].lower()
                        show_db(sortKey)
                except IndexError:
                    print('Enter show (Name/Age/Score)')

            elif parse[0] == commands[3]: # quit
                write_db()
                break

            elif parse[0] == commands[4]: # find
                name = input('Enter the name: ') if len(parse) == 1 else parse[1]
                find_db(name)

            elif parse[0] == commands[5]: # inc
                try:
                    if len(parse) == 1:
                        name = input('Enter the name: ')
                        amount = input('Enter the increasing amount: ')
                    else:
                        name = parse[1]
                        amount = parse[2]
                except IndexError:
                    print('Enter inc (name) (amount)')
                inc_db(name, amount)

        else: # non exsist command
            print('Invalid command: ' + parse[0])
            print('Exsist commands: ')
            for command in commands:
                print(command, end = ', ')
            print()

while True:
    file_name = 'assignment3.dat'
    try:
        db = read_db()
        do_db()
        break
    except FileNotFoundError:
        import os
        print('File not found')
        print(os.getcwd())
        print(file_name)
        break
    except UnicodeDecodeError:
        print("File cannot decode")
        break
    except UnicodeEncodeError:
        print("File cannot encode")
        break