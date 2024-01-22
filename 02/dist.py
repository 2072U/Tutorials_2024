#Author: Lennaert van Veen, Ontario Tech U.
#Date: 1/17/2023
# Python function that computes the distance travelled by a cannon ball with air friction.
# In: theta, angle of the shot; c, coefficient of air friction;
# g, accelleration of gravity; V0, initial speed. See lecture 3.
# A solution of dist=R is the angle at which to tilt the canon for given c, g and V0.
import numpy as np

def dist(theta,c,g,V0):
    return (1/c) * np.log((c*V0*np.cos(theta)/np.sqrt(c*g)) *                    \
                       (np.arctan(np.sqrt(c/g)*V0*np.sin(theta)) +                 \
                        np.arccosh(np.sqrt((g+c* V0**2 * np.sin(theta)**2)/g)))+1.0)


