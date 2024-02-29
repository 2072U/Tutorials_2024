# Example solution to the programming part of tutorial 6, MATH/CSCI2072U, Ontario Tech U, 2024.
import numpy as np

# Compute the normal matrix for a set of nodes x.
def normal(x):
    n = np.shape(x)[1] - 1                         # Extract n.
    V = np.zeros([n+1,n+1])                        # Allocate Vandermonde and normal matrices.
    N = np.zeros([n+1,n+1])
    for i in range(0,n+1):
        for j in range(0,n+1):                     # Note, that this is not optimal (see tutorial 7).
            V[i,j] = x[0,i]**j
    for i in range(0,n+1):
        for j in range(i,n+1):                     # Since the normal matrix is symmetric, we need only compute half the off-diagonal elements.
            for k in range(0,n+1):
                N[i,j] = N[i,j] + V[k,i] * V[k,j]
    for i in range(1,n+1):
        for j in range(0,i):
            N[i,j] = N[j,i]

    return V,N
