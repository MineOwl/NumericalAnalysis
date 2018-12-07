import numpy as np
from numpy import dot



def clearsmallelement(*,npmatrix):
    """
    行列の小さい成分を0にする
    """
    npmatrix = npmatrix.copy()
    npmatrix[abs(npmatrix) < 1e-3] = 0
    return npmatrix

def QR(A):
    N = len(A)
    R = np.zeros((N,N))
    #POINT:配列は通常の=では同じ中身をさしてしまうためcopyしなくていいけない
    Q = np.eye(N = N)
    Q[:,0] = A[:,0] / np.linalg.norm(A[:,0])
    R[0,0] = np.linalg.norm(A[:,0])

    for i in range(1,N):
        #Qを求める
        #   PNを作る
        Sum = 0
        for j in range(0,i):
            Sum -= dot(  (A[:,i]@Q[:,j])  , Q[:,j])
        Pn = A[:,i] + Sum
        PNnorm = np.linalg.norm(Pn)
        Q[:,i] = Pn / PNnorm
        #WARN:なぜか富豪が入れ替わる
        for j in range(0,i):
            R[j,i] = A[0:,i]@Q[0:,j]
        #Rを求める
        R[i,i] = PNnorm
        
    return Q,R

"""
                    _    __                       _                   
 _ __ ___  __ _  __| |  / _|_ __ ___  _ __ ___   | |__   ___ _ __ ___ 
| '__/ _ \/ _` |/ _` | | |_| '__/ _ \| '_ ` _ \  | '_ \ / _ \ '__/ _ \
| | |  __/ (_| | (_| | |  _| | | (_) | | | | | | | | | |  __/ | |  __/
|_|  \___|\__,_|\__,_| |_| |_|  \___/|_| |_| |_| |_| |_|\___|_|  \___|
"""
A = [
        [ 5, 4, 1 , 1],
        [ 4, 5, 1 , 1],
        [ 1, 1, 4 , 2],
        [ 1, 1, 2 , 4]
    ]

A = np.array(A)
while True:
    #ステップ3    表示
    """
    print("actual num is")
    print(A)
    """
    
    print("cleared small num")
    print( clearsmallelement(npmatrix = A) )
    _ = input()

    #ステップ１　　Q,R分解する
    Q, R = QR(A)

    #ステップ２　　R*Qを計算しそれをAとしてステップ２へ
    A = np.dot(R,Q)
