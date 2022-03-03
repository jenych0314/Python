from sys import stdin

for i in range(1, 4):
    globals()[f'x{i}'], globals()[f'y{i}'] = map(int, stdin.readline().strip().split())

