from matplotlib import pyplot as plt
import numpy as np

path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면\\PythonWork\\DAlpha\\1-2'#input('파일경로를 입력해주세요: ')
fname = 'busan_illegal_park.txt'

def main(path, fname):
    with open(path + '\\\\' + fname,'r', encoding = 'utf-8-sig', newline = '') as f:
        f.readline()

        temp_list = []
        cnt = []

        for line in f:
            temp = line.split(',')
            temp_list.append(str(temp[1]))
        
        dates = list(set(temp_list))
        dates.sort()

        for date in dates:
            cnt.append(temp_list.count(date))
            
    plt.figure(figsize = (16, 9))
    plt.bar(dates, cnt, color='white', edgecolor='black')

    plt.xlabel('dates')
    plt.ylabel('count')
    
    plt.xticks(rotation = 90)

    plt.tight_layout()
    plt.show()#그래프 출력 및 메모리에서 제거

if __name__ == '__main__':
    main(path, fname)