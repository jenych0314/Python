import os
import pickle
import math

# 이 함수를 구현하시면 됩니다


def get_cos_sim(vector1, vector2):  # 코사인 유사도 구하는 함수
    similarity = 0  # 유사도 초기화
    # vector가 평면 벡터인지 입체 벡터인지 모름.
    #cosx = (a1*b1 + a2*b2) / {(a1**2 + a2**2)**(1/2) * (b1**2 + b2**2)**(1/2)}
    # cosx -> similarity
    return similarity

# Function 1


def same_label_avg(data, label):
    avg = 0
    for idx in range(len(data[label]) - 1):
        avg += get_cos_sim(data[label][idx], data[label][idx + 1])
    avg = avg / len(data[label])
    return avg

# Function 2


def diff_label_avg(data, label1, label2):
    avg = 0
    for vector1, vector2 in zip(data[label1], data[label2]):
        avg += get_cos_sim(vector1, vector2)
    avg = avg / min(len(data[0]), len(data[2]))
    return avg


def main():
    data = dict()
    print("Loading data...")

    # Phase 1
    with open(f"{os.curdir}{os.sep}DAlpha{os.sep}1-3{os.sep}data{os.sep}label.csv", "r") as csv:
        csv.readline()
        for line in csv:
            name, label = line.split(',')
            label = int(label[:-1])
            if label not in data:
                data[label] = []

            # Phase 2
            with open(rf'{os.curdir}{os.sep}DAlpha{os.sep}1-3{os.sep}data{os.sep}{name}{os.extsep}pkl', 'rb') as f:
                data[label].append(pickle.load(f))

    command = "init"
    print("""Usage
    get [a] [b] --> print average cosine similarity between a and b
    get [a] --> print average cosine similarity with a
    quit --> quit program
    """)
    while command != "quit":
        command = input(">>> ").split()
        if command[0] not in ["get", "quit"] or len(command) > 3:
            print("wrong command")
            continue
        if len(command) == 2:
            ret = same_label_avg(data, int(command[1]))
            print(f"avg: {ret:.20f}")
        elif len(command) == 3:
            ret = diff_label_avg(data, int(command[1]), int(command[2]))
            print(f"avg: {ret:.20f}")
        elif command == "quit":
            break


if __name__ == '__main__':
    main()
