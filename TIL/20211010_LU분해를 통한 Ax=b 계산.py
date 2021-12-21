import numpy as np
from numpy.ma.core import masked_invalid

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print('---', msg, '---')
    n, m = A.shape
    for i in range(0, n):
        line = ''
        for j in range(0, m):
            line += '{0:.2f}'.format(A[i, j]) + '\t'
        print(line)
    print()

def gauss(Ab):
    n, m = A.shape

    for i in range(n):
        maxEl = abs(A[i, i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k, i]) > maxEl:
                maxEl = abs(A[k,i])
                maxRow = k
    
        for k in range(i, m):
            tmp = A[maxRow, k]
            A[maxRow, k] = A[i, k]
            A[i, k] = tmp
        
        piv = A[i, i]
        for k in range(i, m):
            A[i, k] = A[i, k]/piv
        
        for k in range(n):
            if k != i:
                c = A[k, i]/A[i, i]
                for j in range(i, m):
                    if i == j:
                        A[k, j] = 0
                    else:
                        A[k, j] = A[k, j] - c * A[i, j]
        
        pprint(str(i+1) + "번째 반복", A)

#LU 분해 함수
def LU(A):
    n, m = A.shape
    L = np.zeros((n, n)) # 행렬 L 초기화
    U = np.zeros((n, n)) # 행렬 U 초기화

    # 행렬 L과 U 계산
    for i in range(n):
        for j in range(i, n):
            # print('U{}{} = A{}{} = {}'.format(i+1,j+1, i+1,j+1, A[i, j]))
            U[i, j] = A[i, j]
            for k in range(i):
                # print('U{}{} = U{}{} - L{}{} * U{}{} = {} - {} * {} = {}'.format(i+1,j+1, i+1,j+1, i+1,k+1, k+1,j+1, U[i, j], L[i, k], U[k, j], U[i, j] - L[i, k] * U[k, j]))
                U[i, j] = U[i, j] - L[i, k] * U[k, j]
        
        L[i, i] = 1
        if i < n - 1:
            p = i + 1
            for j in range(p):
                # print('L{}{} = A{}{} = {}'.format(p+1,j+1, p+1,j+1, A[p, j]))
                L[p, j] = A[p, j]
                for k in range(j):
                    # print('L{}{} = L{}{} - L{}{} * U{}{} = {} - {} * {} = {}'.format(p+1,j+1, p+1,j+1, p+1,k+1, k+1,j+1, L[p, j], L[p, k], U[k, j], L[p, j] - L[p, k] * U[k, j]))
                    L[p, j] = L[p, j] - L[p, k] * U[k, j]
                # print('L{}{} = L{}{} / U{}{} = {} / {} = {}'.format(p+1,j+1, p+1,j+1, j+1,j+1, L[p, j], U[j, j], L[p, j] / U[j, j]))
                L[p, j] = L[p, j] / U[j, j]

    return L, U

# LU 분해를 이용한 Ax = b의 해 구하기
def LUSolver(A, b):
    L, U = LU(A)
    n = len(L)

    # Ly = b 계산
    y = np.zeros((n, 1))
    for i in range(0, n):
        y[i] = b[i]
        for k in range(0, i):
            y[i] -= y[k] * L[i, k]
    
    # Ux = y 계산
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        if i < n - 1:
            for k in range(i + 1, n):
                x[i] -= x[k] * U[i, k]
        x[i] = x[i] / float(U[i, i])
    
    return y, x

# 행렬 A의 i행과 j열을 제거하고 만든 행렬 생성
def getMinorMatrix(A, i, j):
    n = len(A)
    M = np.zeros((n - 1, n - 1))

    for row in range(n - 1):
        k = row if (row < i) else row + 1
        for col in range(n - 1):
            l = col if (col < j) else col + 1
            M[row, col] = A[k, l]
    
    return M

# 행렬식 계산
def determinant(M):
    if len(M) == 2: # 2*2 행렬의 행렬식 계산
        return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    
    detVal = 0
    for i in range(len(M)):
        detVal += ((-1) ** i) * M[0, i] * determinant(getMinorMatrix(M, 0, i))
    
    return detVal

# 여인수 계산
def cofactor(A, i, j):
    n, m = A.shape
    M = np.zeros((n - 1, m - 1))

    for a in range(n - 1):
        k = a if (a < i) else a + 1
        for b in range(m - 1):
            l = b if (b < j) else b + 1
            M[a, b] = A[k, l]
    
    return (-1) ** (i + j) * np.linalg.det(M)

# 수반행렬 만들기
def adjMatrix(A):
    n, m = A.shape
    adjA = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            adjA[j, i] = cofactor(A, i, j)
    
    return adjA

# 수반행렬을 이용한 A의 역행렬 계산
def inverseByAdjoinMatrix(A):
    detA = np.linalg.det(A)
    
    adjA = adjMatrix(A)
    if detA != 0:
        return (1/detA) * adjA
    else:
        return 0
    
# 크래머 공식을 이용한 연립선형방정식 Ax=b의 풀이
def solveByCramer(A, bVector):
    X = np.zeros(len(bVector))
    C = np.copy(A)

    for i in range(len(bVector)):
        for j in range(len(bVector)):
            C[j, i] = bVector[j]
            if i > 0:
                C[j, i - 1] = A[j, i - 1]
        X[i] = np.linalg.det(C)/np.linalg.det(A)
    return X

# 행렬곱 구하기
# AB = np.matmul(A, B)

# 역행렬 구하기
# way 1 = np.linalg.matrix_power(matrix, -1)
# way 2 = np.linalg.inv(matrix)

# 행렬식 구하기
# np.linalg.det(matrix)

A = np.array([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
b = np.array([[1], [3], [-1]])

invA = np.linalg.inv(A)
adjA = adjMatrix(A)

pprint("adj", adjA)
pprint("inv", invA)

x = np.matmul(invA, b)
pprint("x", x)