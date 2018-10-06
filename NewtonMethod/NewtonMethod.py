#!/bin/sh
import numpy as np
import matplotlib.pyplot as plt

def func1(x):

    return x**2 -2


def func2(x):
        
    return x**3 - x**2 + 10


def func3(x):

    return (-x)**3 -1


def func4(x):

    return 
    x-np.sin(x) -1

def func5(x):

    return x-np.e**(-x)
        



def main(*,count, Xzero , h , f):
    """
        using :::(  f(x+h) - f(x)  ) / h
    """
    def funcdash(h,f,x):
        return (  f(x+h) - f(x)  ) / h

    Xn = 1
    Isforplot =[]
    Xsforplot =[]
    for i in range(10):
        #Xnplus1 = Xn - f(Xn)/funcdash( h, f, Xn)

        Reverse_LinerinterPolation = (Xn - Xzero) / (f(Xn) - f(Xzero))
        Xnplus1 = Xn - f(Xn)*Reverse_LinerinterPolation

        Xn = Xnplus1
        print(i,"->",Xn)
        Xsforplot.append(Xn)
        Isforplot.append(i)


    plt.plot(Isforplot,Xsforplot)
    plt.show()
    return Xnplus1



if __name__ == "__main__":
    ans = main(count=10 , Xzero=10 , h=0.01 , f=func5 )
    print("ans = ",ans)
