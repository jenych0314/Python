arr = [1,2,3,2,1,2,3,2,1,2,3,2,1,2,3,2,1,2,3]

# arr.remove(3)

# while 3 in arr:
    # arr.remove(3)
#내가 찾고자 하는 것이 앞부분에 몰려있다. -> 효율적
#내가 찾고자 하는 것이 골고루 분포되어있다. -> 비효율적

# for i in range(arr.count(3)):
#     arr.remove(3)
#내가 찾고자 하는 것이 앞부분에 몰려있다. -> 비효율적
#내가 찾고자 하는 것이 골고루 분포되어있다. -> 효율적

print(arr)