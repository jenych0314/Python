#1
numbers = list(map(int, input().split()))

current_sum = 0

for i in numbers:
    current_sum += i

print("Sum value: ", current_sum)
print("Average value: ", current_sum/len(numbers))


#2
score_db = [{'name': 'lee', 'score': 30}, {'name': 'kim', 'score': 60}, {'name': 'park', 'score': 50}, {'name': 'jeon', 'score': 40}]

print('min: ', min(score_db, key = lambda person: person['score']))
print('max: ', max(score_db, key = lambda person: person['score']))