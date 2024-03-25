# Starter code for tutorial 10 on boundary value problems, MATH/CSCI2072U, Ontario Tech U, 2024, by L. van Veen.
#from scipy.sparse.linalg import spsolve # Uncomment if you want to exploit the sparsity of the linear system.
#import scipy.sparse as sps
import numpy as np
import matplotlib.pyplot as plt

def f(x):                                                                  # Right-hand-side of the boundary value problem.
    return  x *np.sin(x)

def u(x):                                                                  # Exact solution for comparison.
    return -2.0 + 2.0*np.cos(x)+x*np.sin(x)+(np.pi+1.0)*x

n = 1
ntrials = 1                                                                # Try ntrials difference grid sizes.
err = np.zeros((ntrials,2))                                                # Allocate array to store errors.

for k in range(0,ntrials):                                                 # Loop over grid sizes.
    n *= 10                                                                # Increase number of grid points.
    h = np.pi/float(n)                                                     # Compute grid spacing.
    xs = np.linspace(0,np.pi,n+1)                                          # Define grid points.

    # Fill the matrix:
    M = np.zeros( ... )
    for i in range( ... ):
        M[ ... ] = ...
        ...
        
    # Or, if you want to exploit the sparsity:
#    d0 = 
#    d1 = 
#    d2 = 
#    d3 =     
#    M = sps.diags([d0,d1,d2,d3],[-2,-1,0,1])

    R = f(xs[1:n+1])                                                       # Set right-hand side to f on the grid and boundary values.
    R[n-1] =                                                               # Set the right value at the right boundary.
    # Solve the linear problem:
    w = np.linalg.solve( ... )
    # Or, when using the sparse linear algebra package:
#    w = spsolve(M,R)                                                       

    err[k,0] = n
    err[k,1] = np.linalg.norm( ... )                                       # Store the grid size and the error.
print(err)

# Plot the results
plt.loglog(err[:,0],err[:,1],'-k*',err[:,0],err[:,0]**(-2),'-r')
plt.xlabel('number of grid points')
plt.ylabel('error of solution')
plt.title('Red line indicates O(h^2)')
plt.show()
