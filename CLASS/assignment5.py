import pickle

data_base = []

def read_db():
    global data_base
    with open('{}/{}'.format(file_path, file_name), 'rb') as f:
        data_base = pickle.load(f)
        for data in data_base:
            data['Age'] = int(data['Age'])
            data['Score'] = int(data['Score'])
    return data_base

def write_db(data_base):
    with open('{}/Modified_{}'.format(file_path, file_name), 'wb') as f:
        pickle.dump(data_base, f)

def show_db(data_base, keyname):
    for p in sorted(data_base, key = lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + ' = ' + str(p[attr]), end = ' ')
        print()

def find_db(data_base, name):
    name = name[0].upper() + name[1:].lower()
    cnt = 0

    for p in data_base:
        if p['Name'] == name:
            for attr in sorted(p):
                print(attr + ' = ' + str(p[attr]), end = ' ')
            print()
            cnt += 1

    if cnt == 0:
        print('Cannot find ', name)

def inc_db(name, amount):
    global data_base

    try:
        name = name[0].upper() + name[1:].lower()
        amount = int(amount)
        for p in data_base:
            if p['Name'] == name:
                p['Score'] += amount
        return data_base
    except ValueError:
        print('Enter the amount integer')

def add_db(name, age, score):
    global data_base

    name = name[0].upper() + name[1:].lower()
    try:
        record = {'Name':name, 'Age':int(age), 'Score':int(score)}
        data_base += [record]
        return data_base
    except ValueError:
        print('Enter the age and score integer')

def del_db(name):
    global data_base

    name = name[0].upper() + name[1:].lower()
    for p in data_base:
        if p['Name'] == name:
            data_base.remove(p)
            
    return data_base
    
def do_db(data_base):
    while True:
        input_str = input('DB > ')

        if input_str == '': continue

        parse = input_str.split(' ')
        commands = ['add', 'del', 'show', 'quit', 'find', 'inc']

        if parse[0] == commands[0]: # add
            try:
                add_db(parse[1], parse[2], parse[3])
            except IndexError:
                print('Type \'add name age score\'')

        elif parse[0] == commands[1]: # del
            name = input('Enter the name: ') if len(parse) == 1 else parse[1]
            del_db(name)

        elif parse[0] == commands[2]: # show
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            show_db(data_base, sortKey)

        elif parse[0] == commands[3]: # quit
            break

        elif parse[0] == commands[4]: # find
            name = input('Enter the name: ') if len(parse) == 1 else parse[1]
            find_db(data_base, name)

        elif parse[0] == commands[5]: # inc
            if len(parse) == 1:
                name = input('Enter the name: ')
                amount = input('Enter the increasing score amount: ')
            else:
                name = parse[1]
                amount = parse[2]
            inc_db(name, amount)

        else: # non exsist command
            print('Invalid command: ' + parse[0])
            print('Exsist commands: ')
            for command in commands:
                print(command, end = ', ')
            print()

while True:
    file_path = input('Enter the file path: ')
    file_name = 'assignment3.dat'
    try:
        db = read_db()
        do_db(db)
        write_db(db)
        break
    except FileNotFoundError:
        print('File not found')
        continue
    except UnicodeDecodeError:
        print("File cannot decode")
        continue
    except UnicodeEncodeError:
        print("File cannot encode")
        continue