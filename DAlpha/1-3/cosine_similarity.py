"""
D-Alpha KISA Project 1-3
Similarity: Cosine Similarity

유사하다, 라는 것은 뭘까요?
돌고래와 범고래는 유사하고, 말라뮤트와 허스키도 유사하지만 컴퓨터를 멍청해서 이걸 수치로 나타내 주어야 합니다.

"유사도"를 구하기 위한 방법은 여러 가지가 있지만, 이번에 소개할 유사도는 Cosine 을 이용한 Cosine Similarity 입니다.
두 벡터가 이루는 각도가 작으면, 유사하다고 보는 것이지요. 이 각도는 어떻게 구할까요?

여러분이 알고 계시는 벡터의 내적에서, 벡터의 내적은 다음과 같이 나타납니다.
A • B = |A||B|cos(θ) 이죠, 여기에서 두 벡터가 이루는 각도 θ에 주목하면, 위 식은 다음과 같이 나타낼 수 있습니다.
cos(θ) = (A • B) / (|A||B|)
요 cos(θ)의 값이 바로 코사인 유사도입니다!

당연히 1와 -1 사이의 값을 가지고, 1에 가까울수록 유사하다고 보는 것이지요.

===오늘의 숙제===
MNIST 라는 0부터 9까지의 숫자가 써 있는 28 * 28를 제공하는 데이터가 있습니다.
저는 이 이미지를 인공지능을 이용해 어느 숫자인지 알아맞히는 모델을 만들었고, 분류하기 직전의 벡터를 중간에 뱉게 만들었지요.

오늘의 목표는
1. 코사인 유사도를 구해주는 함수를 구현하고,
2. Function 들의 역할에 주석을 달고 (간단히)
3. Phase 들의 역할에 주석을 달아주시고
4. 코사인 유사도가 가장 낮은 두 숫자를 (예, 1과 3)를 찾아주시면 됩니다! <-- for 문을 이용해도 됩니다.

"""

import os
import pickle


# 이 함수를 구현하시면 됩니다
def get_cos_sim(vector1, vector2):#코사인 유사도 구하는 함수
    similarity = 0#유사도 초기화
    
    return similarity

# Function 1
def same_label_avg(data, label):#같은 label 평균 구하기
    avg = 0#평균값 = 0
    for idx in range(len(data[label]) - 1):#순서
        avg += get_cos_sim(data[label][idx], data[label][idx + 1])
    avg = avg / len(data[label])
    return avg


# Function 2
def diff_label_avg(data, label1, label2):#다른 label의 평균 구하기
    avg = 0
    for vector1, vector2 in zip(data[label1], data[label2]):#zip이란 내장 함수를 이용하여 label1과 label2를 묶음.
        avg += get_cos_sim(vector1, vector2)
    avg = avg / min(len(data[0]), len(data[2]))
    return avg


def main():
    data = dict()
    print("Loading data...")

    # Phase 1
    with open(f"{os.curdir}{os.sep}data{os.sep}label.csv", "r") as csv:
        csv.readline()
        for line in csv:
            name, label = line.split(',')
            label = int(label[:-1])
            if label not in data:
                data[label] = []

            # Phase 2
            with open(rf'{os.curdir}{os.sep}data{os.sep}{name}{os.extsep}pkl', 'rb') as f:
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
