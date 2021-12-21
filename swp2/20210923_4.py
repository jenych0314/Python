# def solution(lst):
#     ans = []
#     dic = {}

#     for num in lst:
#         if num in dic:
#             dic[num] += 1
#         else:
#             dic[num] = 1
    
#     if (max(dic.values()) == 1) or (max(dic.values()) == len(lst)):
#         return []
#     else:
#         for k, v in dic.items():
#             if v == max(dic.values()):
#                 ans.append(k)
#     return ans

# def solution(lst):
#     dic = {k: lst.count(k) for k in set(lst)}

#     if (len(dic) == 1) or (len(dic) == len(lst)):
#         return []
#     else:
#         ans = []
#         for k, v in dic.items():
#             if v == max(dic.values()):
#                 ans.append(k)
#     return ans

def solution(lst):
    dic = {k: lst.count(k) for k in set(lst)}

    if (len(dic) == 1) or (len(dic) == len(lst)):
        return []
    else:
        val_max = max(dic.values())
    return [i for i in dic.keys() if dic[i] == val_max]

lst = list(map(int, input().split()))

print(solution(lst))