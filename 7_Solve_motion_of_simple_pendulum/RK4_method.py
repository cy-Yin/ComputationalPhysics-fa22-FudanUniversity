# python 3.8.13
# RK4_method.py

# Created on Nov 20 19:06:42 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Numerically solve the motion of a simple pendulum
# using RK4 method.


import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 1
g = 9.80
l = 20

def f(x, t):
    return np.array([x[1], -g / l * math.sin(x[0])])

def RK4(f, x0, v0, t, step):
    X_t = np.zeros((len(t), 2))
    X_t[0] = [x0, v0]
    for i in range(len(t) - 1):
        k1 = f(X_t[i], t[i])
        k2 = f(X_t[i] + step / 2 * k1, t[i] + step / 2)
        k3 = f(X_t[i] + step / 2 * k2, t[i] + step / 2)
        k4 = f(X_t[i] + step * k3, t[i] + step)
        X_t[i + 1] = X_t[i] + 1 / 6 * step * (k1 + 2 * k2 + 2 * k3 + k4)
    return X_t

if __name__ == '__main__':
    step = 0.1
    t = np.arange(0, 60, step) # consider the motion period from 0 to 60 seconds.
    x0 = math.pi / 6           # set the initial location at pi/6
    v0 = 0                     # set the initial speed as 0

    # Calculate the total energy.
    X_t = RK4(f, x0, v0, t, step)
    x = X_t[:, 0]
    v = X_t[:, 1]
    Energy = np.zeros(len(t))
    for i in range(len(Energy)):
        Energy[i] = m * g * l * (1 - math.cos(x[i])) + 1 / 2 * m * (l * v[i])**2

    # Plot the angle as a function of time.
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle('RK4 Method')
    plt.subplot(1, 2, 1)
    plt.plot(t, x)
    plt.xlabel(r'$t(s)$')
    plt.ylabel(r'$\theta(rad)$')
    plt.title('angle as a function of time')
    # Plot the energy as a function of time.
    plt.subplot(1, 2, 2)
    plt.plot(t, Energy - Energy[0], 'r')
    plt.xlabel(r'$t(s)$')
    plt.ylabel(r'$\Delta E (J)$')
    plt.title('energy as a function of time')
    plt.show()
