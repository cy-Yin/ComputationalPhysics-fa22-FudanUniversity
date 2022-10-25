# python 3.8.13
# question1.py

# Created on Oct 17 22:26:42 2022
# @author: yinchaoyang
# --- utf-8 ---

# Use the Newton Interpolation and Cubic Spline Interpolation Method
# to interpolate the function Cos(x) with the given points.

import numpy as np
import matplotlib.pyplot as plt

import NewtonInterpolation
import CubicSplineInterpolation


points_x = np.linspace(0, np.pi, 10)
points_y = np.cos(points_x)

# newton interpolation
x1 = np.linspace(0, np.pi, 1000)
y1 = NewtonInterpolation.newtonInterpolation(points_x, points_y, x1)
plt.plot(x1, y1, 'r', alpha=0.8, label='Newton Interpolation')
plt.scatter(points_x, points_y, label='Data Points')
plt.legend(loc='best')
plt.show()

# cubic spline interpolation
DD_function_x2 = CubicSplineInterpolation.cubicSpine(points_x, points_y)
for i in range(len(points_x) - 1):
    x_i = np.linspace(points_x[i], points_x[i + 1], 100)
    y_i = DD_function_x2[i] / (6 * (points_x[i + 1] - points_x[i])) * (points_x[i + 1] - x_i)**3 + \
        DD_function_x2[i + 1] / (6 * (points_x[i + 1] - points_x[i])) * (x_i - points_x[i])**3 + \
        (points_y[i] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i] * (points_x[i + 1] - points_x[i]) / 6) * (points_x[i + 1] - x_i) + \
        (points_y[i + 1] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i + 1] * (points_x[i + 1] - points_x[i]) / 6) * (x_i - points_x[i])
    if i == 0:
        plt.plot(x_i, y_i, 'r', alpha=0.8, label = "Cubic Spline")
    else:
        plt.plot(x_i, y_i, 'r', alpha=0.8)
plt.scatter(points_x, points_y, label='Data Points')
plt.legend(loc='best')
plt.show()

# Compare the newton interpolation with the real function.
plt.plot(x1, y1 - np.cos(x1), 'r', alpha=0.8, label='Newton Interpolation')
plt.legend()
plt.show()

# Compare the newton interpolation with the real function.
for i in range(len(points_x) - 1):
    x_i = np.linspace(points_x[i], points_x[i + 1], 100)
    y_i = DD_function_x2[i] / (6 * (points_x[i + 1] - points_x[i])) * (points_x[i + 1] - x_i)**3 + \
        DD_function_x2[i + 1] / (6 * (points_x[i + 1] - points_x[i])) * (x_i - points_x[i])**3 + \
        (points_y[i] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i] * (points_x[i + 1] - points_x[i]) / 6) * (points_x[i + 1] - x_i) + \
        (points_y[i + 1] / (points_x[i + 1] - points_x[i]) - DD_function_x2[i + 1] * (points_x[i + 1] - points_x[i]) / 6) * (x_i - points_x[i])
    if i == 0:
        plt.plot(x_i, y_i - np.cos(x_i), 'r', alpha=0.8, label = "Cubic Spline")
    else:
        plt.plot(x_i, y_i - np.cos(x_i), 'r', alpha=0.8)
plt.legend()
plt.show()