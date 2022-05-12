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
    test1 = set()
    for line in f:
        test1.add(line[:-1])
# test.csv에서 file을 집합으로 저장
# test값에 중복이 존재하여 값의 차이를 보임

temp = set(train.keys())
temp = temp & test1
# test와 train의 file에 교집합을 구함

ans = []
for i in temp:
    ans.append(train.get(i))

print('0: {}개, 1: {}개'.format(ans.count('0'), ans.count('1')))
print(time() - start_time)
