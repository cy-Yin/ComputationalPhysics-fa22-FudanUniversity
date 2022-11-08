# python 3.8.13
# question2.py

# Created on Oct 29 14:10:03 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Compute the integration with Simpson's rule 
# using Equal spacing grids: r[i]=r0 * [e^(i-1)h - 1]; i = 1, ..., N (try different N)

import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
Z = 14
n = 3
a = 0  # the lower limit of the integral
b = 40 # the upper limit of the integral
r0 = 5e-4

def R_3s(r):
    rho = 2 * Z * r / n
    return  1 / (9 * np.sqrt(3)) * (6 - 6 * rho + rho**2) * Z**(3 / 2) * np.exp(- rho / 2)

def f(r):
    return (R_3s(r) * r)**2

def SimpsonRule(a, b, N):
    h = math.log((b - a) / r0 + 1) / (N - 1)
    r = np.zeros(N + 1)
    t = np.zeros(N + 1)
    for i in range(1, N + 1):
        t[i] = (i - 1) * h
        r[i] = r0 * (np.exp(t[i]) - 1)
    integral = sum((r[2:N + 1] - r[1:N]) / (2 * 3) * (f(r[1:N]) + \
        f(r[2:N + 1]) + 4 * f((r[2:N + 1] + r[1:N]) / 2)))

    return integral

if __name__ == '__main__':
    hs = []
    integrals = []
    numOfPoints = []
    for numOfPoint in range(3, 1000, 2):
        numOfPoints.append(numOfPoint)
        hs.append(math.log((b - a) / r0 + 1) / (numOfPoint - 1))
        integral = SimpsonRule(a, b, numOfPoint)
        integrals.append(integral)
    
    # Find the minimum of numOfPoints that makes the deviation smaller than EPSILON
    # between the calculated integral and the real one.
    EPSILON = 1e-6
    for index in range(len(integrals)):
        if abs(integrals[index] - 1) < EPSILON:
            break
    print("the minimum of numOfPoints that makes the deviation smaller than %f\n"
        "between the calculated integral and the real one is %d\n" % (EPSILON, numOfPoints[index]))
    print("the corresponding integral is", integrals[index])

    # plot the deviation between the calculated integral and the real one 
    # with the different parameter h
    integrals = np.array(integrals)
    plt.plot(numOfPoints, abs(integrals - 1), 'o', markersize=4)
    plt.xlabel("N")
    plt.ylabel("deviation of integral")
    plt.xlim(0, 500)
    plt.show()

