# Example solution to the programming part of tutorial 6, MATH/CSCI2072U, Ontario Tech U, 2024.
import numpy as np
import time                              # For timing.
import matplotlib.pyplot as plt          # For plotting.
from normal import *

ntrials = 6                              # nr. of trials
wtime=np.zeros((ntrials,2))             
n=8
for k in range(0,ntrials):
    X = np.random.rand(1,n)
    start=time.time()                    # Get start time
    N = normal(X)
    elapsed=time.time()-start            # Measure elapsed time
    wtime[k,0] = n
    wtime[k,1] = elapsed
    n = n*2

plt.loglog(wtime[:,0],wtime[:,1],'*-r',wtime[:,0],1E-6*wtime[:,0]**3,'-k')
plt.xlabel('Matrix size')
plt.ylabel('Wall time (s)')
plt.title('Black: order n^3')
plt.show()
