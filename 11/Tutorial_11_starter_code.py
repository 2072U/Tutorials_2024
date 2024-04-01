import numpy as np
import matplotlib.pyplot as plt
from Simpson import simpson

def f(x):                              # Test function
    return np.exp(np.sin(x)+1)

ntest =                                # Compare ntest numbers of intervals
l =                                    # Left and right boundary of the integral
r =  
a = np.zeros((ntest,2))                # Pre-allocate array for approximate results

for k in range(0,ntest):               # Loop over number of intervals
    n =                                # Set number of intervals
    I = simpson( ... )                 # Approximate the integral using composite Simpson
    a[k,0] = n                         # Store result
    a[k,1] = I
print(a)                               # Display results and plot consecutive differences
plt.loglog(a[1:ntest+1,0],abs(np.diff(a[:,1])),'-*',a[1:ntest+1,0],a[1:ntest+1,0]**(-4),'-r')
plt.xlabel('number of intervals')
plt.ylabel('Difference between consecutive approximations')
plt.title('Red line indicates O(1/n^4)')
plt.show()
# Note, that on every interval the error is of order O(h**(-5))=O(1/n**5) and we have n intervals, so the total error decays as O(1/n**4).
