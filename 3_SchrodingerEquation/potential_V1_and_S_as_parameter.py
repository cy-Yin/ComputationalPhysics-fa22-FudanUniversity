# python 3.8.13
# potential_V1_and_S_as_parameter.py.py

# Created on Oct 8 9:34:54 2022
# @author: yinchaoyang
# --- utf-8 ---

# Solve 1D Schrodinger equation with the Potential V(x) = x^2 using a Gaussian basis 
# with a variational parameter: the center of the Gaussian s_i.

import math
import numpy as np
from scipy.linalg import sqrtm # calculate the matrix square root
import matplotlib.pyplot as plt

# constants
h_bar = 1       # reduced Planck constant
m = 0.5          # mass
v = 2 * math.pi
num_of_Basis = 50

# Choose the basis set through change the S parameter.
s = np.linspace(-5, 5, num_of_Basis)

# initialize the S matrix and H matrix, both of which are n*n.
S_ModifiedMatrix = np.zeros((num_of_Basis, num_of_Basis))
Hamilton_matrix = np.zeros((num_of_Basis, num_of_Basis))

def potential(x): # the potential function V(x)
    return x**2

def Integral_Phi_multiply_Phi(si, sj):
    return math.sqrt(v) * math.exp(-v * (si - sj) ** 2 / 2) / math.sqrt(2 * math.pi)

def Integral_Phi_multiply_operatorH_mutiply_Phi(si, sj):
    return math.exp(-v * (si - sj)**2 / 2) * (2 * h_bar**2 * v**2 * (1 - v * (si - sj)**2)\
         + m * (1 + v * (si + sj)**2)) / (4 * m * math.sqrt(2 * v * math.pi))

# Solution of 1D Schrodinger equation
def wave_function(index, s, eigenvectors, x): 
    # wave_function = \sum{j from 1 to n}{eigenvalue_j * phi_j} 
    sum = 0
    for j in range(num_of_Basis):
        sum += -eigenvectors[j][index] * math.sqrt(v / math.pi) * math.exp(-v * (x - s[j])**2)
    return sum

if __name__ == '__main__':
    # calculate the S matrix and H matrix
    for i in range(num_of_Basis):
        for j in range(num_of_Basis):
            S_ModifiedMatrix[i][j] = Integral_Phi_multiply_Phi(s[i], s[j]) # the S matrix
            Hamilton_matrix[i][j] = Integral_Phi_multiply_operatorH_mutiply_Phi(s[i], s[j]) # H matrix
    
    # Todo: calculate the eigenvalues and the corresponding eigenvectors.
    # Hamilton_matrix * eigenvector = eigenvalue * eigenvector
    
    # Since the basis set is not orthogonal, introduce S_ModifiedMatrix.
    # Hamilton_matrix_prime * eigenvector_prime = eigenvalue * eigenvector_prime
    S_ModifiedMatrix_sqrt = sqrtm(S_ModifiedMatrix) # S_{1/2}
    S_ModifiedMatrix_sqrt_inv = np.linalg.inv(S_ModifiedMatrix_sqrt) # S_{-1/2}
    Hamilton_matrix_prime = S_ModifiedMatrix_sqrt_inv @ Hamilton_matrix @ S_ModifiedMatrix_sqrt_inv # H' = S_{-1/2} * H * S_{-1/2}

    eigen_states, eigenvectors_prime = np.linalg.eig(Hamilton_matrix_prime) # calculate the "modified" eigenvalues and eigenvectors
    eigenvectors = S_ModifiedMatrix_sqrt_inv @ eigenvectors_prime # C = S_{-1/2} * C'

    # Find the 3 lowest energy eigenstates.
    eigen_states_3lowest = sorted(eigen_states)[:3]
    indexes = []
    for i in range(3):
        index = np.argwhere(eigen_states == eigen_states_3lowest[i])
        indexes.append(int(index))
    print("The 3 lowest energy eigenstates with potential V(x) = x^2 are: ")
    for i in range(3):
        print("%.4f  " % (eigen_states[indexes[i]]))

    # Plot the wave function.
    fig, ax = plt.subplots()
    x = np.linspace(-4, 4, 1000)
    for i in range(3):
        waveFunction = [wave_function(indexes[i], s, eigenvectors, xi) for xi in x]
        ax.plot(x, waveFunction, label=f"$\phi_{i}$")
    ax.plot(x, potential(x), "k--", label="$V(x) = x^2$")
    ax.legend(loc="upper right")
    ax.set_ylim(-1, 1)
    plt.show()