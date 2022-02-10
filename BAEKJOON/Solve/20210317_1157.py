temp_dict = {}
string = input().lower()

for s in string:
    if s in temp_dict:
        temp_dict[s] = temp_dict[s] + 1
    else:
        temp_dict[s] = 1

temp_keys = list(temp_dict.keys())
temp_values = list(temp_dict.values())
temp_items = list(temp_dict.items())
cnt = 0
temp = 0

for i in range(len(temp_dict)):
    if temp_items[i][1] == max(temp_values):
        cnt += 1
        temp = i

if cnt > 1:
    print('?')
elif cnt <= 1:
    print(str(temp_keys[temp]).upper())