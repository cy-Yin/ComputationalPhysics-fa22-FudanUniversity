# python 3.8.13
# potential_of_hydrogen_atom.py.py

# Created on Nov 28 14:16:04 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Numerically solve the radial Schrodinger equation
# with the potential V.


import numpy as np
import matplotlib.pyplot as plt
import math

Z = 3
r_loc = 0.4
C1 = -14.0093922
C2 = 9.5099073
C3 = -1.7532723
C4 = 0.0834586

def potential(x):
    V = -Z / x * math.erf(x / (math.sqrt(2) * r_loc)) \
        + math.exp(-0.5 * (x / r_loc)**2) \
        * (C1 + C2 * (x / r_loc)**2 + C3 * (x / r_loc)**4 + C4 * (x / r_loc)**6)
    return V

if __name__ == '__main__':
    step = 0.01
    start = 0
    stop = 30
    x = np.arange(start, stop, step)
    num = x.shape[0]

    H = np.zeros((num - 2, num - 2))
    for i in range(num - 2):
        for j in range(num - 2):
            if i == j:
                H[i][j] = 1 / (step**2) + potential(x[i + 1])
            if i == j + 1 or i == j - 1:
                H[i][j] = -1 / (2 * step**2)

    eigenvalues, eigenvectors = np.linalg.eig(H)
    eigenvectors = eigenvectors.T

    eigen_states_3lowest = sorted(eigenvalues)[:3]
    indexes = []
    for i in range(3):
        index = np.argwhere(eigenvalues == eigen_states_3lowest[i])
        indexes.append(int(index))
    
    # Plot the wave function.
    fig, ax = plt.subplots()
    for i in range(3):
        u = np.zeros(num)
        for j in range(1, len(u) - 1):
            u[j] = eigenvectors[indexes[i]][j - 1] 
        ax.plot(x, u, label=f"$E_{i} = {eigenvalues[indexes[i]]}$")
    ax.legend(loc="best")
    plt.xlim((-0.5, 16))
    plt.xlabel(r"$r$")
    plt.ylabel(r"$u(r)$")
    plt.show()

