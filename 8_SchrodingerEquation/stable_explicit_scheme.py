# python 3.8.13
# stable_explicit_scheme.py

# Created on Dec 12 15:12:53 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Use stable explicit scheme 
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
x0_prime = 4.0
dt = 0.005 # time interval for snapshots
t0 = 0.0 # initial time
tf = 0.2 # final time

# Initial Wavefunction
A = 1.0 / (sigma * np.sqrt(np.pi))  # normalization constant
psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)
psi1 = np.sqrt(A) * np.exp(-(x-x0_prime)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)

V = np.zeros(x.shape)
for i, _x in enumerate(x):
    if _x > 9 or _x < 0:
        V[i] = V_hight # potential

t = int(tf / dt)
n = int(10 / dx)
phi = np.zeros((t, n))
phi[0] = psi0
phi[1] = psi1

for i in range(2, t): # stable explicit scheme
    phi[i, 1:n-1] = phi[i-2, 1:n-1] + 1.j * dt / (dx**2) * (phi[i-1, 2:n] + \
        phi[i-1, 0:n-2] - 2*phi[i-1, 1:n-1])

def psi(t, psi):
    F = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2
    return -1j * (-0.5 * hbar / m * F.dot(psi) + V / hbar * psi)
phi = np.zeros((int(tf/dt), int(10/dx)+1), dtype=complex)
sol = integrate.solve_ivp(psi, t_span=[t0, tf], y0=psi0, t_eval=np.arange(t0, tf, dt), method="RK23")

# Plot the wave function and the potential.
fig = plt.figure(figsize=(6, 4))
for i in range(int(tf/dt)):
    plt.plot(x, np.abs(sol.y[:, i])**2) # Plot Wave-functions
    plt.plot(x, V, "k--", label=r"V(x)") # Plot Potential
    plt.ylim(-0.1, 1.5)
    plt.legend(loc=1, fontsize=8, fancybox=False)
    plt.show()
