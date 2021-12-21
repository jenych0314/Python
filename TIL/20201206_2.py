from random import*

user = list(range(1,21))

winner = list((sample(user,4)))

print("1등: %d\n" %winner[0])
print("2등: " + winner[1:])