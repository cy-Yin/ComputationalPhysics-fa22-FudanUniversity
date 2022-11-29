# python 3.8.13
# potential_of_hydrogen_atom.py.py

# Created on Nov 27 09:26:38 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Numerically solve the radial Schrodinger equation
# with the potential V = -1 / r.


import numpy as np
import matplotlib.pyplot as plt

def potential(x):
    V = -1 / x
    return V

if __name__ == '__main__':
    step = 0.01
    start = 0
    stop = 60
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
            u[j] = -eigenvectors[indexes[i]][j - 1] 
        ax.plot(x, u, label=f"$E_{i} = {eigenvalues[indexes[i]]}$")
    ax.legend(loc="best")
    plt.xlim((-2, 60))
    plt.xlabel(r"$r$")
    plt.ylabel(r"$u(r)$")
    plt.show()

