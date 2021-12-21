"""
D-Alpha KISA Project 1-1
CSV 파일 다루기

open 함수는 파일의 헤더를 리런해주는 함수입니다
open(file, mod, buffering, encooing, errors, newline, closedfd, opener)
file: 파일 위치
mod: r, w, x, a, b, t, + (읽기, 쓰기, 베타 쓰기, 추가, 이진 모드, 덱스트 모드, 업데이트 모드)
encoding: 파일 인코딩
예를 들어
open("hello.txt", "r") 함수는 hello.txt 파일을 읽기 위한 파일을 리턴해주고,
open("hello.txt", "w") 힘수는 hello.txt 파일을 생성하고 그 파일에 내용을 씁니다. 이때 같은 이름의 파일이 존재하면 원래 파일을 덮어쓰기 주의하세요
그림, 실행 파일과 같은 이진 파일은 open("notepad.exe", "rb") 같이 이진 모드로 읽으면 되겠죠

위 함수의 사용법은 두 가지가 있습니다.
===1번 방법===
fh = open("C:\Windows\...\hello.txt", "r")
fh.write("hello, world!\n") --> 읽기 모드라 이런 행위를 하면 당연히 오류가 발생합니다.
...
fh.close()

===2번 방법===
with open("C:\Windows\...\hello.txt", "r") as f:
    data = f.readline()
with 블록이 끝나면 자동으로 파일이 닫힙니다! 저는 이 방법을 선호해요
print(data)

파일 객체에서 주로 쓰는 함수는 다음과 같습니다
f.read(size) --> 파일을 size만큼 읽습니다. size에 아무것도 주지 않으면 전부 읽고요
f.readline() --> 파일을 한 줄 읽습니다.
f.readlines() --> 파일의 내용이 포함된 리스트를 반환합니다. newline(보통 '\n')으로 각 원소들이 분리됩니다.
f.write() --> 파일에 내용을 씁니다.

오늘의 숙제
train.csv 파일의 내용을 읽어서 적절한 형식으로 저장한 후에, test.csv 파일에 몇개의 1과 0이 있는지 출력하는 프로그램을 만들면 됩니다.
예를 들어, train.csv 파일에
87518bd9fc387ea079fd5f5175b13a8ce271a2cdec1548995b7bfc3ed18a354c,0
과 같은 내용이 있으면, test.csv에 만약 같은 이름(87518bd9fc387ea079fd5f5175b13a8ce271a2cdec1548995b7bfc3ed18a354c) 이 있다면
0이 하나 있는 것이지요.
"""


def main():
    print("===read()=== 결과")
    with open("demo.csv", "r") as f:
        print(f.read())

    print("===readline()=== 결과")
    with open("demo.csv", "r") as f:
        print(f.readline())

    print("===readlines()=== 결과")
    with open("demo.csv", "r") as f:
        print(f.readlines())

    print("===응용===")
    with open("demo.csv", "r") as f:  # 파일을 읽기 모드로 읽고
        f.readline()  # 한 줄 버리고
        for line in f:  # 파일이 끝날 떄 까지 한 줄씩 읽을건데
            file, label = line.split(",")  # 한 줄을 콤마로 분리한다 (csv는 comma separated values의 약자입니다)
            # 이떄, label의 끝에 '\n'이 붙는거에 주의하세요!
            print(f"file: {file}, label: {label[:-1]}")  # 그 결과를 이용해 출력


if __name__ == '__main__':
    main()
