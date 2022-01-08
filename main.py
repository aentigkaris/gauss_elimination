"""
Ntigkaris E. Alexandros
Python v.3.9.2

Gauss matrix elimination using pivoting.
"""

import numpy as np

# Input
A = np.array([[1,-1,2,-1,-8],[2,-2,3,-3,-20],[1,1,1,0,-2],[1,-1,4,3,4]])
N = len(A)

print(f"\nOriginal matrix:\n{A}\n")

for j in range(N):

    # Pivoting
    if A[j,j] == 0:
        key = np.argmax(abs(A[:,j]))
        temp = np.zeros(N+1)
        if j != key:
            temp[:] = A[j,:]
            A[j,:] = A[key,:]
            A[key,:] = temp[:]

    # Elimination        
    for i in range(1,N-j): A[i+j,:] = A[i+j,:] - (A[i+j,j]/A[j,j] * A[j,:])

print(f"Augmented Gaussian matrix:\n{A}\n")

# Solutions
x = np.zeros(N)
x[-1] = A[N-1,N]/A[N-1,N-1]

for i in reversed(range(N-1)):
    sum = 0
    for j in range(i+1,N):
        sum += A[i,j]*x[j]
    x[i] = (A[i,N] - sum)/A[i,i]

print(f"Solutions:\n{x}\n")