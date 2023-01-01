# python 3.8.13
# calculate_volume_of_hypersphere_MC_method.py

# Created on Dec 29 21:56:12 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# for a given temperature, calculate the magnetization as the function of time
# plot magnetization-timesteps graph.

import numpy as np
import matplotlib.pyplot as plt

from FccFMCurieTemperature_HeisenbergSpinModel_MCmethod import kB, J, time_start, time_stop, time_step
from FccFMCurieTemperature_HeisenbergSpinModel_MCmethod import randomly_orientated_3D_vector, fcc_heisenberg_spin_model, randomly_choose_and_change_a_spin, decide_the_new_spins


def fcc_heisenberg_spin_model_orgin_state():
    spin = np.zeros((30, 30, 30, 3)) # 15*15*15 cubes, 3 as the dimension of every vector
    for i in range(30):
        for j in range(30):
            for k in range(30):
                if (i + j + k) % 2 == 0:
                    # Originally, all the spin are set as (1, 0, 0)
                    spin[i][j][k] = np.array([1, 0, 0])
                else:
                    spin[i][j][k] = np.zeros(3)
    return spin

def magnetization_with_a_given_temperature(chosen_temperature, start, stop, step):
    time = np.arange(start, stop, step)
    magnetization = np.zeros(len(time))
    # Originally, all the spin are set as (1, 0, 0)
    original_spin = fcc_heisenberg_spin_model_orgin_state()

    spin = original_spin
    for t in time:
        spin = decide_the_new_spins(spin, chosen_temperature)
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

    return time, magnetization


if __name__ == '__main__':
    chosen_temperature = 80
    time, magnetization = magnetization_with_a_given_temperature(chosen_temperature,\
                                             time_start, time_stop, time_step)

    # Plot magnetization-timesteps.
    plt.plot(time, magnetization)
    plt.xlabel("Timesteps")
    plt.ylabel("Magnetization")