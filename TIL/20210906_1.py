hello = ['h', 'e', 'l', 'l', 'o']
print(list(enumerate(hello)))
# enumerate, 순서값과 요소값 둘을 한꺼번에 구해 주는 내장 함수
# 순서값은 0부터 시작하지만, 두 번째 인수로 시작값을 지정하면 이 값에서 시작한다.

A = ['a1', 'a2', 'a3']
B = ['b1', 'b2', 'b3', 'b4']
C = list(zip(A, B))
D = dict(zip(A, B))
print(C)
print(D)
# 여러 개의 컬렉션을 합쳐 하나로 만든다. 두 리스트의 대응되는 요소끼리 짝을 지어 튜플의 리스트를 생성한다.
# 두 리스트의 길이가 다를 경우, 짧은 쪽의 길이에 맞추어지며 긴 쪽의 남는 요소는 사용하지 않는다.

lst1 = [True, True, False, None, True]
print(any(lst1)) # any, 리스트를 순회하며 참인 요소가 하나라도 있는지 조사한다
print(all(lst1)) # all, 리스트의 모든 요소가 참인지 조사한다.

lst2 = []
print(any(lst2)) # 참이 하나도 없다고 판단해 거짓으로 평가함
print(all(lst2)) # 거짓이 하나도 없다고 판단해 참으로 평가함

# filter 함수는 리스트의 요소 중 조건에 맞는 것만 골라낸다.
# 첫 번째 인수는 조건을 지정하는 함수
# 두 번째 인수는 대상 리스트
def flunk(score):
    return score < 60
score = [45, 89, 72, 53, 94]
for s in filter(flunk, score):
    print(s)

# map 함수는 모든 요소에 대해 변환 함수를 호출해 새 요소값으로 구성된 리스트를 생성한다.
def half(n):
    return n/2

score = [45, 89, 72, 53, 94]
for s in map(half, score):
    print(s, end = ' ')

# lst = map(int, input())

# lambda 인수:식, 이름이 없고 입력과 출력만으로 함수를 정의하는 축약된 방법
score = [45, 89, 72, 53, 94]
for s in filter(lambda x:x<60, score):
    print(s)

score = [45, 89, 72, 53, 94]
for s in map(lambda x:x/2, score):
    print(s, end = ', ')

lst1 = [1,2,3]
lst2 = lst1
lst2[1] = 100
print(lst1)
print(lst2)

lst1 = [1,2,3]
lst2 = lst1.copy()
#copy 메서드는 원본 리스트와 똑같은 리스트를 새로 생성하여 리턴한다.
lst2[1] = 100
print(lst1)
print(lst2)

import copy
lst0 = ['a', 'b']
lst1 = [lst0, 1, 2]
lst2 = copy.deepcopy(lst1)
lst2[0][1] = 'c'
print(lst1)
print(lst2)
# 완전한 사본을 만들려면 깊은 복사를 수행해야 하는데 이때는 copy 모듈의 deepcopy 함수를 사용한다.

# 두 변수가 같은 객체를 가리키고 있는지 조사할 때 is 구문을 사용한다.
# 좌우 변수가 똑같은 객체를 가리키고 있으면 True를 리턴하고 그렇지 않다면 False를 리턴한다.