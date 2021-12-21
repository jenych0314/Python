import pickle

path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면\\PythonWork'
filename = 'dump1.dat'

# with open(path + '\\\\' + filename,'wb') as f:
#     pickle.dump({'waiver':'권리 포기, 면제', 'tution':'수업료'}, f)

with open(path + '\\\\' + filename,'rb') as f:
    dic = pickle.load(f)
    print(dic)