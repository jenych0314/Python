def solution(v):
    answer = []

    answer.append(v[0][0]^v[1][0]^v[2][0])
    answer.append(v[0][1]^v[1][1]^v[2][1])
    
    return answer