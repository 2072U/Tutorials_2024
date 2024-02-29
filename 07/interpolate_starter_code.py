# Starter code for tutorial 7, MATH/CSCI2072U, Onterio Tech U, 2024.
import numpy as np

# In: 1D arrays x and y of length n, the interpolation data.
# Out: array a of polynomial coefficients so that the interpolant is P(x)= a[0] + a[1] * x + ... + a[n] * x^n.
def intpl(x,y):
    n =                    # Extract the polynomial order of interpolation.
    V =                    # Allocate (n+1) by (n+1) array for the Vandermonde Matrix.
    for i in range( ... ):
        ...
        for j in range( ...):
                           # Assign elements of the Vandermonde matrix.
    c = np.linalg.cond(V,2)
    a =                    # Solve for the coefficents (use our LUP module or np.linalg.solve).
    return a, c
