#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

b=0.3

def henon(x,y,a):
    return 1-a*x*x+y, b*x

def sim(a):
    x=0.5
    y=0.2
    for i in np.arange(1000):
        x,y = henon(x,y,a)
    n=1000
    u=np.zeros((n,2))
    for i in np.arange(n):
        x,y = henon(x,y,a)
        u[i,0]=x
        u[i,1]=y
    plt.plot([a]*n,u[:,0],'.',
             color=[0,0,0],
             markersize=0.005)
plt.figure()
a_vals = np.linspace(1.,1.4,1000)
for a in a_vals:
    sim(a)
plt.show()

