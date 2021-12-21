"""
D-Alpha KISA Project 1-2
matplotlib 의 pyplot 다루기

참조 링크
https://wikidocs.net/92071

========================================================================================
오늘의 숙제
busan_illegal_park.csv 파일을 읽어서
위반일자를 기준으로 2020-01-01부터 2020-12-31까지의 일별 위반 개수를 그래프를 나타내기 또는,
동을 기준으로 각 동별 위반 개수를 막대그래프로 나타내기

둘 다 split을 잘 활용하면 됩니다.
========================================================================================
"""

# 오늘의 주인공을 import 합니다
# from A import B as C의 의미는 A 패키지에서 모듈 B를 C라는 이름으로 사용하겠다는 선언입니다.
from matplotlib import pyplot as plt


def main():
    # 어제 했던 csv 파일 읽기를 이용해서 csv 파일을 읽고
    with open('demo.csv', 'r') as f:
        f.readline()
        val1 = []
        val2 = []
        for line in f:
            temp = line.split(",")
            val1.append(float(temp[0]))
            val2.append(float(temp[1]))

    # 도화지(figure) 하나를 만들어줍니다 이걸 선언해주지 않으면 기본 도화지가 생성됩니다.
    # 도화지 크기(figsize)는 모니터 비율에 맞게 16, 9 로 설정해봤어요
    plt.figure(figsize=(16, 9))

    # matploblib.pyplot(이하 plt)의 plot 함수는 다음과 같이 사용합니다.
    # plot(x 좌표(들), y 좌표(들), ...) ...에는 정말 많은 파라미터가 들어갈 수 있으니 참조 링크를 봐주세요!
    plt.plot(range(len(val1)), val1, linestyle='solid', label='sin')
    plt.plot(range(len(val2)), val2, linestyle='solid', label='cos')

    # plt의 legend 함수는 그래프의 범례를 표시해줍니다.
    plt.legend()

    # plt의 show 함수는 여태 그려진 그래프를 출력해주고, 여태 그려진 그래프를 메모리에서 버립니다.
    plt.show()

    # 추가적으로, plt의 bar 함수는
    # bar(변량(들), 도수(들), ...) 여기의...에도 정말 많은 파라미터가 들어갈 수 있으니 참조 링크를 봐주세요!
    # ex> bar(["2020-01-01", "2020-01-02", ..., "2020-12-31"], [100, 230, 132, 123, 211, 314, ... 123])


if __name__ == '__main__':
    main()
