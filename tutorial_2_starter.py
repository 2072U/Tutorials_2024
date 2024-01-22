# Starter code for Tutorial 2.
import numpy as np
import matplotlib.pyplot as plt
from dist import dist          # Function from the cannonball problem (lec 3).
from bisect import bisect      # Simple implementation of bisection.
# from secant import secant      # Write this one yourself!

# Set the parameters:
c = 0.001 # Coefficient of drag.
v0 = 40   # Initial speed of the cannonball.
g = 9.81  # Accelleration of gravity in SI units.
R = 100   # Distance to the target in metres.

# Try to solve for a zero of this function:
def f(x):
    return dist(x,c,g,v0) - R

# Plot first to get an idea of a good initialization of our iterative methods:
xs = np.linspace(0,np.pi/2,100)
ys = np.zeros((100,1))
for i in range(0,100):
    ys[i] = f(xs[i])

plt.plot(xs,ys)
plt.show()

# Initial left and right boundary:
a = 
b = 
print('Setting a=%f and b=%f to start bisection...' % (a,b))
# max nr. of iterations and target error and residual:
kMax = 
tolX = 
tolF = 
x,recordB = bisect( ... )
print('Setting x0=%f and x1=%f to seed secant iteration...' % (a,b))
kMax = 
# Make sure your secant function returns the errors and residuals in the same format as the bisection function!
x,recordS = secant()

plt.semilogy(recordB[:,0],recordB[:,1],'o')
plt.semilogy(recordS[:,0],recordS[:,1],'o')
plt.show()

plt.semilogy(recordB[:,0],recordB[:,2],'o')
plt.semilogy(recordS[:,0],recordS[:,2],'o')
plt.show()
