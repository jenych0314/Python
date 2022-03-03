import time
import random

def sorted_list_merge(lst1, lst2):
    lst1_pos = 0
    lst2_pos = 0
    merged_lst = []
    while (lst1_pos < len(lst1)) and (lst2_pos < len(lst2)):
        if lst1[lst1_pos] > lst2[lst2_pos]:
            merged_lst += [lst2[lst2_pos]]
            lst2_pos += 1
        else:
            merged_lst += [lst1[lst1_pos]]
            lst1_pos += 1

    #1
    # while lst1_pos < len(lst1):
    #     merged_lst += [lst1[lst1_pos]]
    #     lst1_pos += 1

    # while lst2_pos < len(lst2):
    #     merged_lst += [lst2[lst2_pos]]
    #     lst2_pos += 1
    
    #2
    if lst1_pos < len(lst1):
        merged_lst += lst1[lst1_pos:]

    if lst2_pos < len(lst2):
        merged_lst += lst2[lst2_pos:]
    
    return merged_lst

lst1 = sorted([random.randint(1, 99999) for i in range(100000)])
lst2 = sorted([random.randint(1, 99999) for i in range(100000)])

ts = time.time()
lst3 = sorted(lst1 + lst2)
print(time.time() - ts)

ts = time.time()
lst3 = sorted_list_merge(lst1, lst2)
print(time.time() - ts)