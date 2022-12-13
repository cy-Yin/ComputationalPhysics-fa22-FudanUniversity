# python 3.8.13
# stable_explicit_scheme.py

# Created on Dec 12 13:04:12 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Use Crank-Nicolson scheme 
# to solve the one-dimensional schrodinger equation 
# with its potential as a square wall
# with a Gaussian initial state coming in from the left.

import numpy as np
from scipy import integrate
from scipy import sparse
import matplotlib.pyplot as plt

# Set initial conditions
dx = 0.005 # spatial separation
x = np.arange(0, 10, dx) # spatial grid points
kx = 50 # wave number
m = 1 # mass
hbar = 1
V_hight = 1000000
sigma = 1 # width of initial gaussian wave-packet
x0 = 3.0 # center of initial gaussian wave-packet

# Initial Wavefunction
A = 1.0 / (sigma * np.sqrt(np.pi))  # normalization constant
psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)

V = np.zeros(x.shape)
for i, _x in enumerate(x):
    if _x > 9 or _x < 0:
        V[i] = V_hight # potential

def psi_t(t, psi): # the H matrix for the Crank-Nicolson scheme
    # Laplace Operator (Finite Difference)
    D2 = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2
    return -1j * (-0.5 * hbar / m * D2.dot(psi) + V / hbar * psi)

dt = 0.005 # time interval for snapshots
t0 = 0.0 # initial time
tf = 0.2 # final time
t_eval = np.arange(t0, tf, dt)  # recorded time shots
phi = np.zeros((int(tf/dt), int(10/dx)+1), dtype=complex)
sol = integrate.solve_ivp(psi_t, t_span=[t0, tf], y0=psi0, t_eval=t_eval, method="RK23")

# Plot the wave function and the potential.
fig = plt.figure(figsize=(6, 4))
for i in range(int(tf/dt)):
    plt.plot(x, np.abs(sol.y[:, i])**2) # Plot Wave-functions
    plt.plot(x, V, "k--", label=r"V(x)") # Plot Potential
    plt.ylim(-0.1, 1.5)
    plt.legend(loc=1, fontsize=8, fancybox=False)
    plt.show()