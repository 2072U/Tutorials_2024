# Starter code for the interpolation test script, tutorial 7, MATH/CSCI2072U, Ontario Tech U, 2024.
import numpy as np
import matplotlib.pyplot as plt          # For plotting
from interpolate import *

def f(x):                                # Test function
    return np.exp(x)               

# In: float x, list of polynomial coefficients a.
# Out: the value of a[0] + a[1] * x + ... + a[n] * x^n.
def P(x,a):                              # Evaluate interpolant using Horner's algorithm (lec 10, slides 10-13).
    n = np.shape(a)[0]-1
    Q = a[n-1] + a[n] * x
    for k in range(n-2,-1,-1):
        Q = Q * x + a[k]
    return Q

cond =                                   # Allocate array for storing condition numbers.
for n in range( ...):                    # Loop over numbers of nodes.
    x =                                  # Allocate arrays for the interpolation data.
    y =
    for i in range( ... ):               # Set interpolation data.
        x[i] =
        y[i] =
    a, c = intpl( ... )
    cond[ ... ] = n
    cond[ ... ] = c
    nplot = 1000                         # Number of points for plotting.
    xs = np.linspace(0,float(n),nplot)   # x-values for plotting.
    yf = ...                             # Allocate array for function values f(x).
    yp = ...                             # Allocate array for interpolant values P(x).
    for i in range(nplot):               # Evaluate function and interpolant on nplot grid point for plotting.
        yf[i] = f(xs[i])
        yp[i] = P(xs[i],a)
    plt.plot(xs,yf,'-k',xs,yp,'-r')
    plt.show()

# Now plot the condition number as a function of n:
plt.semilogy( ... )
plt.show()
