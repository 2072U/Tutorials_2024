import numpy as np
import scipy.interpolate as intp  # SciPy has more interpolation functions than NumPy.
import matplotlib.pyplot as plt

def f(x):                      # Test function
    return np.arctan(5.0*x)

Nplot = 1000
xs = np.linspace(-2,2,Nplot) # Grid for plotting

N0 = 
N1 = 
Ntest = 
errs = np.zeros((Ntest,3))

# Spline interpolation:
for n in range(N0,N1+1):
    N = 2**n                                                      # Fix nr. of knots.
    x =                                                           # The locations of the knots.
    y =                                                           # The y-values at the knots.
    S = intp.CubicSpline( ... )                                   # Using the spline function from SciPy.interpolate.
    ys = S.__call__(xs)                                           # This SciPy function returns a PPoly object, this is how to evaluate the interpolant.
    plt.plot(xs,f(xs),'-k',label='f(x)')
    plt.plot(xs,ys,'-r',label='cubic spline on '+str(N)+' knots') # Plot with legend.
    plt.ylim([-2,2])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    e = abs( ... )                                                 # Estimate the error on the fine grid.
    plt.title('|f(x)-S_N(x)| for N='+str(N))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.plot(xs,e,'-r')
    plt.show()
    errs[n-N0,0] = float(N)                                        # Remember the error to compare the methods.
    errs[n-N0,1] = np.max(e)

# That still doesn't look nice, the error increases near the boundary. Try differnt nodes..

for n in range(N0,N1+1):
    N = 2**n
    x = 2.0*np.cos(np.linspace(0,N,N+1) * np.pi/float(N))           # Set the interpolation nodes.
    y =                                                             # Compute the corresponding y-values.
    ys =                                                            # Use an in-built function or our own..
    plt.plot(xs,f(xs),'-k',xs,ys,'-r')
    plt.ylim([-2,2])
    plt.show()
    e = abs(f(xs)-ys)
    plt.plot(xs,e,'-r')
    plt.show()
    errs[n-N0,2] = np.max(e)

plt.loglog(errs[:,0],errs[:,1],label='error of spline interpolation')
plt.loglog(errs[:,0],errs[:,2],label='error of nonuniform interpolation')
plt.xlabel('nr. of knots/nodes')
plt.ylabel('error')
plt.legend()
plt.show()
