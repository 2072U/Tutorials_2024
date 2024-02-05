import numpy
import numpy.linalg
import matplotlib.pyplot as plt          # For plotting

smin =                                   # Set minimal and maximal matrix size
smax = 
rrs = numpy.ones(smax-smin+1)            # Pre-allocate arrays for relative residual,
res = numpy.ones(smax-smin+1)            # relative error and
mes = numpy.ones(smax-smin+1)            # maximal error

for n in range(smin,smax+1):             # Loop over matrix sizes
    xe =                                 # Exact solution
    xe[0] =          
    A = numpy.zeros((n,n))               # Allocate and fill A
    for i in range( ... ):               
        for j in range( ... ):
            A[i-1,j-1] = 
    r =                                  # Set right-hand side
    x =                                  # Solve by LUP decomposition

    rrs[n-smin] =                        # Store relative residual, error and maximal error
    res[n-smin] = 
    mes[n-smin] = 


plt.semilogy(range(smin,smax+1),res,'-b',range(smin,smax+1),mes,'-r')
plt.xlim([smin,smax])
plt.xlabel('matrix size')
plt.ylabel('(maximal) relative error')
plt.title('Maximal (red) and actual (blue) relative error')
plt.show()
