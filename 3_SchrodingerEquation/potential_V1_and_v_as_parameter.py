# python 3.8.13
# potential_V1_and_v_as_parameter.py.py

# Created on Oct 10 13:58:32 2022
# @author: yinchaoyang
# --- utf-8 ---

# Solve 1D Schrodinger equation with the Potential V(x) = x^2 using a Gaussian basis 
# with a variational parameter: the width of the Gaussian v_i.

import math
import numpy as np
from scipy.linalg import sqrtm # calculate the matrix square root
import matplotlib.pyplot as plt

# constants
h_bar = 1       # reduced Planck constant
m = 0.5         # mass
s = 0
num_of_Basis = 10

# Choose the basis set through change the S parameter.
v = np.linspace(1, 11, num_of_Basis)

# initialize the S matrix and H matrix, both of which are n*n.
S_ModifiedMatrix = np.zeros((num_of_Basis, num_of_Basis))
Hamilton_matrix = np.zeros((num_of_Basis, num_of_Basis))

def potential(x): # the potential function V(x)
    return x**2

def Integral_Phi_multiply_Phi(vi, vj):
    return math.sqrt(vi * vj) / math.sqrt(math.pi * (vi + vj))

def Integral_Phi_multiply_operatorH_mutiply_Phi(vi, vj):
    return math.sqrt(vi * vj) * (2 * h_bar**2 * vi * vj + 2 * m * s**2 * (vi + vj) + m)\
         / (2 * m * (vi + vj)**(3 / 2) * math.sqrt(math.pi))

# Solution of 1D Schrodinger equation
def wave_function(index, v, eigenvectors, x): 
    # wave_function = \sum{j from 1 to n}{eigenvalue_j * phi_j} 
    sum = 0
    for j in range(num_of_Basis):
        sum += eigenvectors[j][index] * math.sqrt(v[j] / math.pi) * math.exp(-v[j] * (x - s)**2)
    return sum

if __name__ == '__main__':
    # calculate the S matrix and H matrix
    for i in range(num_of_Basis):
        for j in range(num_of_Basis):
            S_ModifiedMatrix[i][j] = Integral_Phi_multiply_Phi(v[i], v[j]) # the S matrix
            Hamilton_matrix[i][j] = Integral_Phi_multiply_operatorH_mutiply_Phi(v[i], v[j]) # H matrix
    
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
        waveFunction = [wave_function(indexes[i], v, eigenvectors, xi) for xi in x]
        ax.plot(x, waveFunction, label=f"$\phi_{i}$")
    ax.plot(x, potential(x), "k--", label="$V(x) = x^2$")
    ax.legend(loc="upper right")
    ax.set_ylim(-1, 1)
    plt.show()