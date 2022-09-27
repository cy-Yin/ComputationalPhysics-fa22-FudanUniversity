# python 3.8.13
# Solve_and_Plot.py

# Created on Sep 24 16:58:23 2022
# @author: yinchaoyang
# version: 2.0
# --- utf-8 ---

# Determine M(T) the magnetization as a function of temperature T
# for simple magnetic materials.

import matplotlib.pyplot as plt
import numpy as np

import FindrootThroughHybrid as Hybrid


# ------------ Situation 1: 0 < t < 1 ------------ #

# store the "t : m(t)"s for 0 < t < 1
m1 = {}
m2 = {}

t = 1e-2 # initial value for t
while 0 < t < 1:
    root1 = Hybrid.Hybrid(t, -1, 0) # find root1 for tanh(x / t) - x == 0
    root2 = Hybrid.Hybrid(t, 0 , 1) # find root2 for tanh(x / t) - x == 0
    m1[t] = root1
    m2[t] = root2
    t = t + 1e-4 # step of t

keys1 = [key for key, value in m1.items()] 
keys2 = [key for key, value in m2.items()]
values1 = [value for key, value in m1.items()] # every root1 for a given t
values2 = [value for key, value in m2.items()] # every root2 for a given t


# --------------- Situation 2: t >= 1 ------------- #
# when t > 1, m == 0
keys3 = np.arange(1, 2, 0.001)
values3 = [0] * len(keys3)


# ------------------- Plot m(t) ------------------ #
fig, ax = plt.subplots()
ax.plot(keys1, values1, color = 'r')
ax.plot(keys2, values2, color = 'r')
ax.plot(keys3, values3, color = 'r')
plt.xlabel('t')
plt.ylabel('m(t)')
plt.title('reduced magnetization as a function of t')
plt.show()
