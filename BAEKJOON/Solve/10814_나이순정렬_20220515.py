import sys
input = sys.stdin.readline

n = int(input())

data = dict()
for i in range(1, 201):
    data.setdefault(i, [])

for i in range(n):
    age, name = input().split()
    age = int(age)
    data[age].append(name)

for k, v in data.items():
    if v:
        for member_name in v:
            print(f'{k} {member_name}')
