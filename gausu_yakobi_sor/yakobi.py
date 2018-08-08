

import numpy as np

def jacobi(A, b, tol):
    # 線形連立方程式をヤコビ法で解く
    xOld = np.empty_like(b)
    error = 1e12

    D = np.diag(A)
    R = A - np.diagflat(D)
    count=0
    while error > tol:
        x = (b-np.dot(R, xOld))/D
        error = np.linalg.norm(x-xOld)/np.linalg.norm(x)
        xOld = x
        count+=1
    print(count,"回です")
    return x

A = np.array([[7 , -1, 0, 1],
              [-1, 9, -2, 2],
              [0, -2, 8, -3],
              [1, 2, -3, 10]])
b = np.array([-5, 15, -10, 20])

x = jacobi(A, b, 1e-9)
print(x)

