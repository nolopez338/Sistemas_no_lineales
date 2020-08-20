# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:08:11 2020

@author: nicol
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(x,t, k, model_type = 1):
    if model_type == 1:
        u = 0 
    if model_type == 2:
        u = -k*x
    if model_type == 3:
        u = -(k*x)**(1/3)
        
    dydt = x + u**3
    return dydt

# initial condition
x0 = 1

# time points
t = np.linspace(0,4)

# solve ODEs
k = 5

model_type = 1
x0 = 0.1
y1 = odeint(model,x0,t,args=(k,model_type))

model_type = 2
x0 = 1
y2 = odeint(model,x0,t,args=(k,model_type))
u2 = -k*y2

model_type = 3
y3 = odeint(model,x0,t,args=(k,model_type))
u3 = -(k*y3)**(1/3)


# plot results
plt.plot(t,y1,'r-',linewidth=2,label='u=0')
plt.plot(t,y2,'b--',linewidth=2,label='u=-kx')
plt.plot(t,y3,'g:',linewidth=2,label='u=-(kx)^(1/3)')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()

plt.plot(t,u2,'r-',linewidth=2,label='u=-kx')
plt.plot(t,u3,'b-',linewidth=2,label='u=-(kx)^(1/3)')
plt.show()





