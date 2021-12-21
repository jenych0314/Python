import math

def prime_num_1(n):#소수 판별 함수 - 에라토스테네스의 체
    #2~n까지의 모든 수에 대해 소수 판별
    arr = [True for i in range(n+1)]
    #처음엔 모든 수가 소수인 것으로 초기화
    for i in range(2, int(math.sqrt(n)) + 1):#2~n의제곱근까지의 모든 수 확인
        if arr[i] == True:#i가 소수인 경우
            #i를 제외한 i의 모든 배수 지우기
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
    
    return [i for i in range(2, n+1) if arr[i]]

def prime_num_2(n):
    arr = [True] * (n+1)

    for i in range(2, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i+1, n+1, i):
                arr[j] = False
    return [i for i in range(2, (n+1)) if arr[i]]

if __name__ == '__main__':
    print(prime_num_2)