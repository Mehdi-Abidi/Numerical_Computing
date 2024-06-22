import numpy as np
def LUdecomp(A):
    if determinant(A)==0:
      print("Matrix is Singular LU decomposition not possible")
      return None
    else:
     n = len(A)
     P = np.eye(n)  # initialize permutation matrix as identity matrix
     L = np.eye(n)
     Lo=np.zeros(n)
     U = np.zeros(n)
     for k in range(0, n-1):
        # Partial pivoting: swap rows to ensure diagonal element is largest absolute value in the column
        max_index = k + np.argmax(np.abs(a[k:, k]))
        if max_index > k:
            A[[k, max_index]] = A[[max_index, k]]
            P[[k, max_index]] = P[[max_index, k]]
        for i in range(k+1, n):
                lam = A[i,k]/A[k,k]
                L[i,k] = lam
                A[i,k+1:n] = A[i,k+1:n] - lam*A[k,k+1:n]
                A[i,k] = 0

    U=np.triu(A)
    Lo=np.tril(A)
    print('LU decomposition of A is given by \n L=\n',np.matrix(L),'and \n U=\n',np.matrix(U),"by using permutation matrix \n P=\n",np.matrix(P),"by using Lower tri matrix using np \n Lo=\n",np.matrix(Lo))
    return
a = np.array([[0, 1, -1],
              [2, -4, 9],
              [1, -2, 1]],dtype=float)
LUdecomp(a)
