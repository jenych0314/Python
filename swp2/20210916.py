import pickle
import sys

def readDB(dbFilePath, dbFileName):
    try:
        with open("{}/{}".format(dbFilePath, dbFileName), 'rb') as f:
            pass
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        pass

def writeDB(dbFileName, scdb):
    with open(dbFileName, "w") as f:
        for p in scdb:
            pinfo = []
            for attr in p:
                pinfo += [attr + ":" + p[attr]]
            line = ",".join(pinfo)
            f.write(line + "\n")

def doDB(scdb):
    while(True):
        inputStr = input("DB > ")
        if inputStr == "": continue
        parse = inputStr.split(" ")
        commands = ["add", "del", "show", "quit"]
        if parse[0] == commands[0]:#add
            record = {}
            scdb += [record]
        elif parse[0] == commands[1]:#del
            pass
        elif parse[0] == commands[2]:#show
            pass
        elif parse[0] == commands[3]:#quit
            pass
        else:
            pass

file_path = 'Python/swp2/samples-20210914'
file_name = 'test3_2.dat'

# try:
#     with open('{}/{}'.format(file_path, file_name), 'rb') as f:
#         scdb = pickle.load(f)
#         for db in scdb:
#             db["Age"] = int(db["Age"])
#             db["Score"] = int(db["Score"])
# except FileNotFoundError as e:
#     print(e)
#     sys.exit()
# else:
#     print("Open DB: ", file_name)