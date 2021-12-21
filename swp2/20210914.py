file_path = 'Python/swp2/samples-20210914'
file_name = input('Enter the file name: ')

wordCnt = {}

f = open('{}/{}'.format(file_path, file_name), 'r', encoding='utf-8')

lines = f.readlines()

for line in lines:
    words = line.split()
    for word in words:
        if word in wordCnt:
            wordCnt[word] += 1
        else:
            wordCnt[word] = 1

f.close()

print(wordCnt)