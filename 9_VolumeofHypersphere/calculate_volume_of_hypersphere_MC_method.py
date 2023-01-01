# python 3.8.13
# calculate_volume_of_hypersphere_MC_method.py

# Created on Dec 19 17:20:23 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Finds the volume of a hypersphere using a Monte Carlo method
# for d = 2, 3, 4, 5

import numpy as np

def calculate_volume(dimension):
    total = int(1e9)
    rand = np.random.rand(total, dimension) # uniform distribution from 0 to 1
    accept = 0
    for i in range(total):
        if np.linalg.norm(rand[i]) <= 1:
            accept += 1
    volume = accept / total * 2**dimension # 0.5 as the radius of the hypersphere
    return volume

if __name__ == '__main__':
    d = int(input("Please input the dimension of the hypersphere: "))
    volume = calculate_volume(d)
    print("The volume of the %d-dimension hypersphere is %f" % (d, volume))