import numpy as np
import numpy.linalg as LA
from tabulate import tabulate

def Gauss_Siedel(A, b, x, tol, N):

    k = 0
    data=[]
    converged = False
    for i in range(len(b)):
        if A[i,i] == 0:
            j = i + np.argmax(np.abs(A[i:, i]))
            A[[i, j]] = A[[j, i]]
            b[[i, j]] = b[[j, i]]

    while k <= N:
        k += 1
        x0 = x.copy()
        data.append([k,x0[0],x0[1],x0[2]])
        for i in range(len(b)):
            Sum = 0  # reset Sum to zero before the inner loop
            for j in range(len(b)):
                if j != i:
                    Sum += A[i,j] * x[j]
            x[i] = (1 / A[i,i]) * (b[i] - Sum)

        if LA.norm(x - x0) < tol:
            converged = True
            print(tabulate(data,headers=['Iter no','x1','x2',"x3"],tablefmt="github"))
            print('Converged! in',k,'no of iterations')
            return None  # exit the while loop if converged

    if not converged:
        print(tabulate(data,headers=['Iter no','x1','x2',"x3"],tablefmt="github"))
        print('Not converged, increase the # of iterations')

A=np.array([[8,8,3],[2,8,5],[3,5,10]],dtype=float)
b=np.array([[14],[5],[-8]],dtype=float)
N=10
tol=0.01
#Initialize for 0th Iteration
x=np.zeros_like(b)
Gauss_Siedel(A,b,x,tol,N)
