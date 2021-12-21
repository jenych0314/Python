path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면\\PythonWork\\test text'
fname = 'Les_Miserables-Victor_Hugo.txt'

expressions = [",", ".", "?", "!", "\'", "\"", "-", "*", ";", ")", "(", "/", ":"]

with open(path + '\\\\' + fname, 'r', encoding='utf-8') as f:
    words = f.read().split()
    wordCnt = {}
    for word in words:
        word = word.upper()
        for expression in expressions:
            if expression in word:
                word = word.replace(expression, '')
        # if word.isalpha() == False:
        #     print(word)
        #     print('False')
        if word not in wordCnt:
            wordCnt[word] = 1
        else:
            wordCnt[word] += 1

# print(wordCnt)
sortedWordCnt = sorted(wordCnt.items(), key = lambda x: x[1])#, reverse=True)
# print(sortedWordCnt)
maxCnt = sortedWordCnt[-1][1]
print(maxCnt)

for Cnt in sortedWordCnt:
    print("{} : {}, {}".format(Cnt[0], str(Cnt[1]), str(Cnt[1]/maxCnt)))