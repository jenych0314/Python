def sorted_list_merge(lst1, lst2):
    pos_1, pos_2 = 0, 0
    sort_nbrs = []

    while pos_1 < len(lst1) and pos_2 < len(lst2):
        if lst1[pos_1] > lst2[pos_2]:
            sort_nbrs += [lst2[pos_2]]
            pos_2 += 1
        else:
            sort_nbrs += [lst1[pos_1]]
            pos_1 += 1
    
    return sort_nbrs

lst1 = [1, 3, 5, 7, 9]
lst2 = [0, 2, 4, 6, 8]

merged_lst = sorted_list_merge(lst1, lst2)

print(merged_lst)