from time import time

path = input('파일경로를 입력해주세요: ')

start_time = time()

fname = 'train.csv'
with open(path + '\\\\' + fname, 'r') as f:
    f.readline()
    train = {}
    for line in f:
        file, label = line.split(',')
        train[file] = label[:-1]
# train.csv에서 file과 label을 묶어 딕셔너리로 저장

fname = 'test.csv'
with open(path + '\\\\' + fname, 'r') as f:
    f.readline()
    test = []
    for line in f:
        test.append(line[:-1])
# test.csv에서 file을 리스트로 저장

ans = []
for i in range(len(test)):
    ans.append(train.get(test[i]))
# test의 file을 train의 key로 value로 뽕아서 ans에 저장

print('0: {}개, 1: {}개'.format(ans.count('0'), ans.count('1')))
print(time() - start_time)
