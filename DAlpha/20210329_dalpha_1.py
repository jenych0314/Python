from time import time

path = input('파일경로를 입력해주세요: ')

start_time = time()

fname = 'train.csv'
with open(path + '\\\\' + fname,'r') as f:
    f.readline()
    train_f = []
    train_l = []
    for line in f:
        file, label = line.split(',')
        train_f.append(file)
        train_l.append(label[:-1])
#train.csv에서 file과 label을 서로 다른 리스트로 저장

fname = 'test.csv'
with open(path + '\\\\' + fname,'r') as f:
    f.readline()
    test = []
    for line in f:
        test.append(line[:-1])
#test.csv에서 file을 리스트로 저장

ans = []
for i in range(len(test)):
    if test[i] in train_f:
        index = train_f.index(test[i])
        ans.append(train_l[index])
#test의 file이 train의 file에 존재한지 확인 후
#존재하는 경우 label값 추출해서 ans에 저장

print('0: {}개, 1: {}개'.format(ans.count('0'), ans.count('1')))
print(time() - start_time)