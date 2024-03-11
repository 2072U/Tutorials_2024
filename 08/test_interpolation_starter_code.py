# Author: L. van Veen, Ontario Tech U, 2024.
# Starter code for tutorial 8.
import numpy as np
import matplotlib.pyplot as plt
from poly_int import poly_int

# Test function (the Runge function):
def f(x):                   
    return 1.0/(1.0+x**2)

# Domain:
l = ...
r = ...
# Grid for plotting:
n_plot =                        # Insert number large enough for producing a smooth plot but not large enough to slow the script down.
x_out = np.linspace(l,r,n_plot) 

# Remember errors for an increasing number of nodes for plotting:
err = []

# Loop over increasing number of grid points:
for n in range( ... ):
    N = 2**n
    # x-values for interpolation:
    x = np.linspace( ... )
    # Corresponding y-values:
    y = f(x)
    # Compute the interpolant on the fine grid using our code:
    y_out = poly_int( ... )
    plt.plot(x_out,f(x_out),'-k',x_out,y_out,'-r')
    plt.ylim([f(l)-1.0,f(r)+1.0])
    plt.xlabel('x')
    plt.ylabel('function and interpolant')
    plt.title('%d equidistant nodes' % (N))
    plt.show()
    e = np.absolute( ... )
    err.append([N,max(e)])
    plt.plot(x_out,e,'-r')
    plt.xlabel('x')
    plt.ylabel('interpolation error')
    plt.title('%d equidistant nodes' % (N))
    plt.show()

# Plot the error of interpolation versus the number of nodes:
err = np.asarray(err)
plt.loglog(err[:,0],err[:,1],'-*')
plt.show()
