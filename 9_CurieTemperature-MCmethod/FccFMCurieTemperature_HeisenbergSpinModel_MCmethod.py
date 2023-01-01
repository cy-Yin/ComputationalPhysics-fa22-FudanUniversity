# python 3.8.13
# FccFMCurieTemperature_HeisenbergSpinModel_MCmethod.py

# Created on Dec 24 14:12:32 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Estimate the ferromagnetic Curie temperature
# of a 3D Face-Centered Cubic lattice 
# using the Heisenberg spin model (adopt periodic boundary condition)
# through the Metropolis Monte-Carlo algorithm.

import numpy as np
import matplotlib.pyplot as plt

# Constants
kB = 1e-2
J = 1
time_start = 0
time_stop = 10000 # consider the system reaches a steady state after a loop of 10000 steps
time_step = 1
nearest_neighbours = 12

def randomly_orientated_3D_vector():
    u = np.random.rand()
    v = np.random.rand()
    theta = 2 * np.pi * u
    phi = np.arccos(2*v-1)
    x = np.sin(theta) * np.sin(phi)
    y = np.cos(theta) * np.sin(phi)
    z = np.cos(phi)
    
    vector = [x, y, z]
    return vector

def fcc_heisenberg_spin_model():
    spin = np.zeros((30, 30, 30, 3)) # 15*15*15 cubes, 3 as the dimension of every vector
    for i in range(30):
        for j in range(30):
            for k in range(30):
                # For the fcc lattice, 8 spins exist in each corner of the cube 
                # with six additional spins positioned at the center of each cube face.
                # In that case, spins in fcc lattice have the characteristics about their coordinates
                # that they just exists where xi + yi + zi = an even number.
                if (i + j + k) % 2 == 0:
                    spin[i][j][k] = randomly_orientated_3D_vector()
                else:
                    spin[i][j][k] = np.zeros(3)

    return spin

def randomly_choose_and_change_a_spin(spin):
    newSpin = np.zeros((30, 30, 30, 3))
    for i_index in range(30):
        for j_index in range(30):
            for k_index in range(30):
                newSpin[i_index][j_index][k_index] = spin[i_index][j_index][k_index]
    i = 0
    j = 0
    k = 1
    while (i + j + k) % 2 != 0: 
        # the spin exists where xi + yi + zi = an even number
        i = np.random.randint(30)
        j = np.random.randint(30)
        k = np.random.randint(30)
    newSpin[i][j][k] = randomly_orientated_3D_vector()  # randomly change a spin

    # Calculate the change of Energy.
    # Firstly consider the periodic boundary condition.
    spin_expand_old = np.zeros((31, 31, 31, 3))
    for i_index in range(30):
        for j_index in range(30):
            for k_index in range(30):
                spin_expand_old[i_index][j_index][k_index] = spin[i_index][j_index][k_index]
    spin_expand_old[30, :30, :30] = spin[0, :, :]
    spin_expand_old[:30, 30, :30] = spin[:, 0, :]
    spin_expand_old[:30, :30, 30] = spin[:, :, 0]
    for m in range(31):
        spin_expand_old[m, 30, 30] = randomly_orientated_3D_vector()
        spin_expand_old[30, m, 30] = randomly_orientated_3D_vector()
        spin_expand_old[30, 30, m] = randomly_orientated_3D_vector()
    spin_expand_new = np.zeros((31, 31, 31, 3))
    for i_index in range(30):
        for j_index in range(30):
            for k_index in range(30):
                spin_expand_new[i_index][j_index][k_index] = newSpin[i_index][j_index][k_index]
    spin_expand_new[30, :30, :30] = spin[0, :, :]
    spin_expand_new[:30, 30, :30] = spin[:, 0, :]
    spin_expand_new[:30, :30, 30] = spin[:, :, 0]
    for m in range(31):
        spin_expand_new[m, 30, 30] = randomly_orientated_3D_vector()
        spin_expand_new[30, m, 30] = randomly_orientated_3D_vector()
        spin_expand_new[30, 30, m] = randomly_orientated_3D_vector()

    energy_old = -J * ( \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i][j-1][k-1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i][j+1][k-1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i][j+1][k+1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i][j-1][k+1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i-1][j][k-1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i+1][j][k-1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i-1][j][k+1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i+1][j][k+1]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i-1][j-1][k]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i+1][j-1][k]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i-1][j+1][k]) + \
        np.dot(spin_expand_old[i][j][k], spin_expand_old[i+1][j+1][k]) \
        )
    energy_new = -J * ( \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i][j-1][k-1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i][j+1][k-1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i][j+1][k+1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i][j-1][k+1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i-1][j][k-1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i+1][j][k-1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i-1][j][k+1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i+1][j][k+1]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i-1][j-1][k]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i+1][j-1][k]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i-1][j+1][k]) + \
        np.dot(spin_expand_new[i][j][k], spin_expand_new[i+1][j+1][k]) \
        )
    Delta_E = energy_new - energy_old

    return newSpin, Delta_E


def decide_the_new_spins(spin, temperature):
    newSpin, Delta_E = randomly_choose_and_change_a_spin(spin)
    p = np.exp(-Delta_E / (kB * temperature))
    if Delta_E < 0:
        newSpin = newSpin # p > 1, accept the change
    else:
        PRN = np.random.rand()
        if p > PRN:
            newSpin = newSpin # accept the change
        else:
            newSpin = spin # reject the change

    return newSpin


def calculate_magnetization(temperature):
    time = np.arange(time_start, time_stop, time_step)
    magnetization = np.zeros(len(time))
    original_spin = fcc_heisenberg_spin_model()

    spin = original_spin
    for t in time:
        spin = decide_the_new_spins(spin, temperature)
        Sx_total = 0
        Sy_total = 0
        Sz_total = 0
        for i in range(30):
            for j in range(30):
                for k in range(30):
                    Sx_total = Sx_total + spin[i][j][k][0]
                    Sy_total = Sy_total + spin[i][j][k][1]
                    Sz_total = Sz_total + spin[i][j][k][2]
        magnetization[t] = np.linalg.norm([Sx_total, Sy_total, Sz_total])

    loop_magnetization = 0
    loop = 0
    for i in range(8000, time_stop, 20):
        loop_magnetization = loop_magnetization + magnetization[i]
        loop = loop + 1
    loop_mean_magnization = loop_magnetization / loop
    return loop_mean_magnization

def plot(x, y):
    plt.plot(x, y, 'o')
    plt.xlabel("Temperature(K)")
    plt.ylabel("Normalized magnetization")
    plt.show()

if __name__ == '__main__':
    T_start = 0
    T_stop = 200
    T_step = 5
    temperature = np.arange(T_start, T_stop, T_step)
    
    magnetizations = []
    for every_T in temperature:
        magnetization = calculate_magnetization(every_T)
        magnetizations.append(magnetization)
    magnetizations = np.array(magnetizations)
    magnetizations = magnetizations / magnetizations[0] # normalize magnetization

    # Plot the results.
    plot(temperature, magnetizations)