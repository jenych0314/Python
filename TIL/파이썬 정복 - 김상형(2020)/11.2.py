#11.2
def flunk(n):
    return n < 60

score = [45, 80, 98, 30, 53]

for s in filter(flunk, score):
    print(s)

def half(n):
    return n/2

score = [45, 80, 98, 30, 53]

for s in map(half, score):
    print(s, end = ', ')
print()

def total(n1, n2):
    return n1 + n2

score = [45, 80, 98, 30, 53]
bonus = [2, 3, 4, 0, 1]

for s in map(total, score, bonus):
    print(s, end = ', ')
print()

lambda x: x+1#이것과
def increase(x):#이것이 같음
    return x+1

score = [45, 80, 98, 30, 53]
for s in filter(lambda x: x<60, score):
    print(s)