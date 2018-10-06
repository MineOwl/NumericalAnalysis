#!/bin/sh
import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return x**3 -2*x**2 -1*x +2



def main(*, maxloop , f , n_dimention , a1 , r0):
    """
    a1 : n-1乗の係数
    r0 : 収束半径
    """
    #pltでのplot専用の配列
    XforPlt =[]
    YforPlt =[]


    def getPHAI(k):
        PHAI = 1
        for isai in range(n_dimention):
            if isai==k:
                continue
            PHAI *= (Xn[k]-Xn[isai])
        return PHAI
    
    #////////////////////////////////////////////////////////////////////////
    #///////変数の説明/////////////////////////////////////////////////////////
    #///////   k   このプログラムでは方程式の解を同時並行で解くことになる/////////////
    #///////       このときXnやxn plus 1 は配列によって管理され、kはその番号である////
    #///////        つまり、「n個ある解のk番目」という使い方をされる/////////////////
    #/////////////////////////////////////////////////////////////////////////

    #メインのコードはここから
    Xn = []
    Xnplus1 = []

    #Xnの初期値
    for k in range(n_dimention):
        Xn.append(   -a1/n_dimention + r0*np.exp(  2j*(k-1)*np.pi / n_dimention + 2j*np.pi / (2*n_dimention)   )  )
        Xnplus1.append(1)

    for _ in range(maxloop):

        #肝心のループの部分
        for k in range(n_dimention):
            #ファイの部分
            PHAI = getPHAI(k)
            Xnplus1[k] = ( Xn[k] - f(Xn[k])/PHAI)
        Xn = Xnplus1
        print(Xn)

        #----plt中
        for xn in Xn:
            XforPlt.append(xn.real)
            YforPlt.append(xn.imag)
        plt.plot(XforPlt , YforPlt,'ro')
        #----plt終了

    plt.show()
    return Xnplus1



if __name__ == "__main__":
    ans = main( maxloop = 200 , f=func1 , n_dimention=3 , a1=-2 , r0=3 )
