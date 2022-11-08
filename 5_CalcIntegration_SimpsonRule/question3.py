# python 3.8.13
# question3.py

# Created on Oct 29 22:10:32 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Compare the results of question1 and question2.

import numpy as np
import matplotlib.pyplot as plt

import question1
import question2
from question1 import f
from question2 import r0
import math

a = 0  # the lower limit of the integral
b = 40 # the upper limit of the integral

if __name__ == '__main__':
    # Plot the function-to-be-integrated.
    x = np.linspace(0, 40, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel(r'$r$')
    plt.ylabel(r'$r^2|R_{3s}(r)|^2$')
    plt.show()

    hs_1 = []
    numOfPoints_1 = []
    integrals_1 = []
    for numOfPoint in range(3, 1000, 2):
        numOfPoints_1.append(numOfPoint)
        hs_1.append((b - a) / (numOfPoint - 1))
        integral = question1.SimpsonRule(a, b, numOfPoint)
        integrals_1.append(integral)
    hs_2 = []
    numOfPoints_2 = []
    integrals_2 = []
    for numOfPoint in range(3, 1000, 2):
        numOfPoints_2.append(numOfPoint)
        hs_2.append(math.log((b - a) / r0 + 1) / (numOfPoint - 1))
        integral = question2.SimpsonRule(a, b, numOfPoint)
        integrals_2.append(integral)

    integrals_1 = np.array(integrals_1)
    integrals_2 = np.array(integrals_2)
    plt.plot(numOfPoints_1, abs(integrals_1 - 1), 'ob', markersize=5, label="q1")
    plt.plot(numOfPoints_2, abs(integrals_2 - 1), 'or', markersize=5, label="q2")
    plt.xlabel("N")
    plt.ylabel("deviation of integral")
    plt.xlim(0, 500)
    plt.legend(loc='best')
    plt.show()