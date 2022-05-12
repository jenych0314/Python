import sys
input = sys.stdin.readline

N = int(input())

dictionary = dict()
for i in range(1, 51):
    dictionary.setdefault(i, [])

for i in range(N):
    word = input().strip()
    if word in dictionary[len(word)]:
        continue
    else:
        dictionary[len(word)].append(word)

for i in range(1, 51):
    if dictionary[i]:
        for elem in sorted(dictionary[i]):
            print(elem)
