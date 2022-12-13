# python 3.8.13
# question2.py

# Created on Dec 11 15:06:21 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Use the relaxation method to solve the poisson equation 
#   \nabla^2 phi(x, y) = -rho(x, y) / epsilon_0
# with the rectangular geometry boundary condition.
# In question2, rho'(x, y) = rho / epsilon_0 = 1, phi(0, y) = phi(l_x, y) = phi(x, 0) = phi(x, l_y) = 0

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Domain
L = 1.
n = 101
h = L/(n-1)
x = y = np.linspace(0,L,n)
X,Y = np.meshgrid(x,y)
max_iter = 500 # the number of iteration

# Source term
rho = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        rho[i][j] = 1
        
# Initialization
u0 = np.ones((n,n)) / 10
u0[0,:] = u0[-1,:] = u0[:,0] = u0[:,-1] = 0

# Gauss-Seidel Iteration Method
def gauss_seidel(u, f, h):
    u_n = u.copy()
    iter = 0
    
    while iter < max_iter:
        for i in range(1,n-1):
            for j in range(1,n-1):
                u_n[i,j] = 0.25*(u_n[i+1,j] + u_n[i-1,j] + u_n[i,j+1] + u_n[i,j-1] - f[i,j]*h*h)
        iter = iter + 1
    
    return u_n

# Plot
fig = plt.figure()
ax = Axes3D(fig)
u_n = gauss_seidel(u0, rho, h)
ax.plot_surface(X,Y, u_n, rstride=5, cstride=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
ax.set_zlim3d(bottom=0,top=0.08)
plt.show()