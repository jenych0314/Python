from time import time

def binary_search(lst, key):#이진 탐색
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low+high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return -1

path = input('파일경로를 입력해주세요: ')

start_time = time()

fname = 'train.csv'
with open(path + '\\\\' + fname,'r') as f:
    f.readline()
    train = []
    for line in f:
        file, label = line.split(',')
        train.append((file, label[:-1]))
#train.csv에서 file과 label을 묶어 리스트로 저장

fname = 'test.csv'
with open(path + '\\\\' + fname,'r') as f:
    f.readline()
    test = []
    for line in f:
        # file = line
        # test.append(file[:-1])
        test.append(line[:-1])
#test.csv에서 file을 리스트로 저장

train.sort()
test.sort()
#이진 검색을 위해 정렬

train_f = []
train_l = []
for i in range(len(train)):
    train_f.append(train[i][0])
    train_l.append(train[i][1])
#정렬 후 train 리스트를 file과 label로 구분

ans = []
for i in range(len(test)):
    index = binary_search(train_f, test[i])
    if index != -1:
        ans.append(train_l[index])
#test의 file이 train의 file에 존재한지 확인 후
#존재하는 경우 label값 추출해서 ans에 저장

print('0: {}개, 1: {}개'.format(ans.count('0'), ans.count('1')))
print(time() - start_time)