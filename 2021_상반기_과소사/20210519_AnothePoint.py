def solution(v):
    answer = []

    x_dic = {}
    y_dic = {}

    for point in v:
        x_dic[point[0]] = 2 if point[0] in x_dic else 1
    for point in v:
        y_dic[point[0]] = 2 if point[0] in y_dic else 1
    
    for key, value in x_dic.items():
        if value == 1:
            answer.append(key)
            break

    return answer