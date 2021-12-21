import pickle


path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면\\PythonWork\\test text'
f = open(path + '\\\\' + 'test3.txt', 'wb', encoding='utf-8')
f.write('hello')
info = pickle.load(f)
pickle.dump(info, f)
f.close()
# index = 0
# f.seek(index)