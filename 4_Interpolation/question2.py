# python 3.8.13
# question2.py

# Created on Oct 18 09:40:21 2022
# @author: yinchaoyang
# --- utf-8 ---

# Use the Newton Interpolation and Cubic Spline Interpolation Method
# to interpolate the function 1 / (1 + 25 * x^2) with the given points.

import numpy as np
import matplotlib.pyplot as plt

import NewtonInterpolation
import CubicSplineInterpolation


def function(x):
    return 1 / (1 + 25 * x**2)

points_x = np.linspace(-1, 1, 10)
points_y = function(points_x)
plt.scatter(points_x, points_y, color='black')

# the real function
x = np.linspace(-1, 1, 1000)
y = function(x)
plt.plot(x, y, 'orange', label='$f(x) = 1 / (1 + 25x^2)$')

# newton interpolation
x1 = np.linspace(-1, 1, 1000)
y1 = NewtonInterpolation.newtonInterpolation(points_x, points_y, x1)
plt.plot(x1, y1, 'r', alpha=0.8, label = "Newton Interpolation")

# cubic spline interpolation
DD_function_x2 = CubicSplineInterpolation.cubicSpine(points_x, points_y)
for i in range(len(points_x) - 1):
    x_i = np.linspace(points_x[i], points_x[i + 1], 100)
    y_i = DD_function_x2[i] / (6 * (points_x[i + 1] - points_x[i])) * (points_x[i + 1] - x_i)**3 + \
        DD_function_x2[i + 1] / (6 * (points_x[i + 1] - points_x[i])) * (x_i - points_x[i])**3 + \
        (points_y[i] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i] * (points_x[i + 1] - points_x[i]) / 6) * (points_x[i + 1] - x_i) + \
        (points_y[i + 1] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i + 1] * (points_x[i + 1] - points_x[i]) / 6) * (x_i - points_x[i])
    if i == 0:
        plt.plot(x_i, y_i, 'b', alpha=0.8, label = "Cubic Spline")
    else:
        plt.plot(x_i, y_i, 'b', alpha=0.8)

plt.legend(loc='best')
plt.show()