# python 3.8.13
# KronigPenney.py

# Created on Nov 12 09:12:37 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Solve the one-dimensional Kronig-Penney problem 
# with Periodic potential V(x) = V(x + a) .
# Find the lowest three eigenvalues of the eigenstates 
# that satisfy phi(x) = phi(x + a) through FFT.

import numpy as np
from numpy.fft import fft

# Constants
a = 1
u0 = 2
l_w = 0.9
l_b = a - l_w

def f(x): # Periodic potential
    if x >= 0 and x < l_w:
        return 0
    if x >= l_w and x <= a:
        return u0

def Integral(i, j, V_prime):
    if i == j:
        integral = 1.5042 * (j - N)**2 + a * V_prime[i - j] # 2 h_bar^2 * pi^2 / (m * a) = 1.5042
    else:
        integral = a * V_prime[i - j]
    
    return integral


if __name__ == '__main__':
    N = 1000
    # Use FFT to calculate the V_q'
    x = np.linspace(0, a, 2 * N + 1)
    V = np.array([f(i) for i in x])
    V_prime = fft(V)
    V_prime = V_prime / len(V_prime) # normalization

    # Calculate the H matrix.
    H = np.zeros((2 * N + 1, 2 * N + 1), dtype=complex)
    rows, columns = H.shape
    for i in range(rows):
        for j in range(columns):
            H[i][j] = Integral(i, j, V_prime)
    
    # Find the lowest three eigenvalues of the eigenstates.
    eigen_states, eigenvectors_prime = np.linalg.eig(H)
    eigen_states = np.sort(np.abs(eigen_states))
    print("The lowest three eigenvalues are")
    for i in range(30):
        print(eigen_states[i])