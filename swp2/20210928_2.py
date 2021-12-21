#1
def seq_search(nums, target):
    for i in range(0, len(nums)):
        if target == nums[i]:
            return i
    return -1

score_db = [{'Name': 'Lee'}]

def find_score_db(scdb, keyname):
    for i in range(len(scdb)):
        if keyname == scdb[i]['Nmae']:
            return i
    return -1

name = input()
idx = find_score_db(score_db, name)
if idx >= 0:
    print(score_db[idx])
else:
    print('no such name')