import numpy as np

A = [[1,  2,  0, -1],
         [3,  7, -1,  3],
         [2,  2,  1,  2]]
A=np.array(A)
N = A.shape[0]
maxn=N
def function(X,number):
    X=np.array(X)
    """
    number=1,2,3
    """
    newdata=[]
    for num in range(number):
        newdata.append(X[num,:])

    for i in range(number,maxn):
        m=X[number-1][number-1]/X[i][number-1]
        newdata.append(-m*X[i,:]+X[number-1,:])

    return np.array(newdata)


def main():
    hai=A
    for jojo in range(1,N):
        hai=function(hai,jojo)
    print(hai)

    last=[]
    for i in reversed(range(0,N)):
        hai=function2(hai,i)
        last.append(hai[-1,:])
    
    for k in last:
        print(k)
def function2(X,number):
    X=np.array(X)
    return_data=[]

    count=0
    print('k'*100)
    for i in reversed(range(number+1)):
        if count==0:
            count+=1
            cutnums=X[i,:]/X[i][number]
            return_data.append(cutnums)
            continue
        m=cutnums*X[i][number]
        return_data.append(X[i,:]-m)
    return_data=list(reversed(return_data))
    return_data=np.array(return_data)
    print(return_data)
    k=input()
    return return_data



if __name__=="__main__":

    main()