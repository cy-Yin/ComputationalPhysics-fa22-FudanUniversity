# python 3.8.13
# midpoint_method.py

# Created on Nov 20 19:03:04 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Numerically solve the motion of a simple pendulum
# using midpoint method.


import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 1
g = 9.80
l = 20

def f(x, t):
    return np.array([x[1], -g / l * math.sin(x[0])])

def midpoint(f, x0, v0, t, step):
    X_t = np.zeros((len(t), 2))
    X_t[0] = [x0, v0]
    for i in range(len(t) - 1):
        X_t[i + 1] = X_t[i] + f(X_t[i] + 0.5 * step * f(X_t[i], t[i]), t[i] + 0.5 * step) * step
        # X[i + 1] = X[i] + func(X[i] + 0.5 * dt * func(X[i], t[i]), t[i] + 0.5 * dt) * dt
    return X_t

if __name__ == '__main__':
    step = 0.1
    t = np.arange(0, 60, step) # consider the motion period from 0 to 60 seconds.
    x0 = math.pi / 6           # set the initial location at pi/6
    v0 = 0                     # set the initial speed as 0

    # Calculate the total energy.
    X_t = midpoint(f, x0, v0, t, step)
    x = X_t[:, 0]
    v = X_t[:, 1]
    Energy = np.zeros(len(t))
    for i in range(len(Energy)):
        Energy[i] = m * g * l * (1 - math.cos(x[i])) + 1 / 2 * m * (l * v[i])**2

    # Plot the angle as a function of time.
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle('Midpoint Method')
    plt.subplot(1, 2, 1)
    plt.plot(t, x)
    plt.xlabel(r't(s)')
    plt.ylabel(r'$\theta(rad)$')
    plt.title('angle as a function of time')
    # Plot the energy as a function of time.
    plt.subplot(1, 2, 2)
    plt.plot(t, Energy, 'r')
    plt.xlabel(r'$t(s)$')
    plt.ylabel(r'$E(J)$')
    plt.title('energy as a function of time')
    plt.show()