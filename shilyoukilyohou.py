import numpy as np
A=np.array([[2,-3,-1,1],
            [6, 3, 2,4],
            [-2,0,1,-2]],dtype=np.float64)
lrow=A.shape[0]
print(A)
for j in range(lrow -1):
    for i in range(j + 1,lrow):
        if(A[i,j]==0):
            continue
        u =A[i,j]/A[j,j]
        A[i,:]=A[i,:] - u*A[j,:]
        print(A)
print(A)
for i in reversed(range(lrow)): #後段代入
    for j in reversed(range(i)):
        if(A[i][i] == 0):
            continue
        u = A[j,i] / A[i,i]
        A[j,:] = A[j,:] - u * A[i,:]
        print(A)
print(A)
for i in range(lrow):
    if(A[i,i] == 0):
        continue
    A[i,:] = A[i,:] / A[i,i]
print(A)

