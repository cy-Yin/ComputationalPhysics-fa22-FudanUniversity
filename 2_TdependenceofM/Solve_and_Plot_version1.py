# python 3.8.13
# Solve_and_Plot.py

# Created on Sep 23 22:49:30 2022
# @author: yinchaoyang
# version: 1.0
# --- utf-8 ---

# Determine M(T) the magnetization as a function of temperature T
# for simple magnetic materials.

import matplotlib.pyplot as plt
import numpy as np

# ----- Solve t(m) and then turn it into m(t) ---- #

# Situation 1: 0 < t < 1
def t(m):
    if m.any() == 0:
        return 1
    else:
        return m / (np.arctanh(m))

values1 = np.linspace(-1, 1, 10000) # m for 0 < t < 1
keys1 = [t(m) for m in values1]     # t for 0 < t < 1

# Situation 2: t >= 1 
# m == 0
keys2 = np.arange(1, 2, 0.001)      # t for t >= 1
values2 = [0] * len(keys2)          # m for t >= 1

# ------------------- Plot m(t) ------------------ #
fig, ax = plt.subplots()
ax.plot(keys1, values1, color = 'r')
ax.plot(keys2, values2, color = 'r')
plt.xlabel('t')
plt.ylabel('m(t)')
plt.title('reduced magnetization as a function of t')
plt.show()