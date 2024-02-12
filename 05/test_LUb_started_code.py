# Author: L. van Veen, UOIT, 2024
# Starter code for the script of tutorial 5.
import numpy as np
import time
import matplotlib.pyplot as plt          # For plotting
import LUb                               # LU-decomposition without pivoting for babded matrices

# Function to create an n X n matrix with band width b.
def create_banded(n,b):
    A =                                  # Allocate array
    d1 =                                 # Create random diagonal
    for i in range( ... ):               # Fill diagonal
        A[i-1,i-1] = d1[i-1]             
    for i in range(1,b+1):               # Loop over sub/super diagonals
        d1 = np.random.rand( ... )       # Create random sub/super diagonals
        d2 = 
        for j in range( ... ):           # Fill sub/super diagonals
            A[j,j-1] = d1[j-1]
            A[j-1,j] = d2[j-1]
    return A

nstart = 
nend =
ntest =
wtnb =                                   # Pre-allocate array to wall times
for q in range(nstart,nend+1):
    n = 2**q                             # Set matrix size for equidistant points on logarithmic scale
    b = 3                                # Fix band width
    A = create_banded(n,b)               # Create banded matrix
    start=time.time()                    # Get start time
    L,U = LUb.LUb(A,b)                   # Compute decomposition
    elapsed=time.time()-start            # Measure and store elapsed time
    wtnb[ ... ] = n
    wtnb[ ... ] = elapsed
    
plt.loglog( ... )
plt.xlabel('Matrix size')
plt.ylabel('Wall time for sparse LU decomposition (s)')
plt.title('Order n')
plt.show()

n = 100
bstart =
bend =
ntest = bend-bstart+1
wtbb = scipy.zeros([ntest,2])
for b in range(bstart,bend):
    A = create_banded(n,b)               # Create banded matrix       
    start=time.time()                    # Get start time
    L,U = LUb.LUb(A,b)                   # Compute decomposition
    elapsed=time.time()-start            # Measure and store elapsed time
    wtbb[ ... ] = b
    wtbb[ ... ] = elapsed
    
plt.loglog( ... )
plt.xlabel('Matrix size')
plt.ylabel('Wall time for sparse LU decomposition (s)')
plt.title('Order b^2')
plt.show()
# For clearer visualization, plot straight lines corresponding to linear and quadratically increasing wall time in both plots for comparison.
