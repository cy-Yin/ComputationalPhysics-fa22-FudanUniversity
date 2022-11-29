# python 3.8.13
# Euler-trapezoidal_method.py

# Created on Nov 20 19:10:09 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Numerically solve the motion of a simple pendulum
# using Euler-trapezoidal method.


import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 1
g = 9.80
l = 20

def f(x):
    return np.array([x[1], -g / l * math.sin(x[0])])

def Euler_trapezoidal(f, x0, v0, t, step):
    x_t = np.zeros((len(t), 100))
    v_t = np.zeros((len(t), 100))
    x_t[0][0] = x0
    v_t[0][0] = v0
    X_t = np.array([x_t, v_t])
    for i in range(len(t) - 1):
        j = 0
        X_t[:, i + 1, 0] = X_t[:, i, 0] + 0.5 * step * (f(X_t[:, i, 0]) + f(X_t[:, i, 0] + step * f(X_t[:, i, 0]))) # predictors
        X_t[:, i + 1, j + 1] = X_t[:, i, j] + 1 / 2 * step * (f(X_t[:, i, j]) + f(X_t[:, i + 1, j + 1])) # correctors
        j = j + 1
        while j < 100 - 1 and abs(x_t[i][j] - x_t[i][j - 1]) > 1e-3:
            X_t[:, i + 1, j + 1] = X_t[:, i, j] + 1 / 2 * step * (f(X_t[:, i, j]) + f(X_t[:, i + 1, j]))
            j = j + 1
    x_t = X_t[0]
    v_t = X_t[1]
    return x_t, v_t

if __name__ == '__main__':
    step = 0.1
    t = np.arange(0, 60, step) # consider the motion period from 0 to 60 seconds.
    x0 = math.pi / 6           # set the initial location at pi/6
    v0 = 0                     # set the initial speed as 0

    # Calculate the total energy.
    x_t, v_t = Euler_trapezoidal(f, x0, v0, t, step)
    Energy = np.zeros(len(t))
    for i in range(len(Energy)):
        Energy[i] = m * g * l * (1 - math.cos(x_t[i][0])) + 1 / 2 * m * (l * v_t[i][0])**2

    # Plot the angle as a function of time.
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle('Euler-trapezoidal Method')
    plt.subplot(1, 2, 1)
    plt.plot(t, x_t[:, 0])
    plt.xlabel(r'$t(s)$')
    plt.ylabel(r'$\theta(rad)$')
    plt.title('angle as a function of time')
    # Plot the energy as a function of time.
    plt.subplot(1, 2, 2)
    plt.plot(t, Energy, 'r')
    plt.xlabel(r'$t(s)$')
    plt.ylabel(r'$\Delta E (J)$')
    plt.title('energy as a function of time')
    plt.show()
