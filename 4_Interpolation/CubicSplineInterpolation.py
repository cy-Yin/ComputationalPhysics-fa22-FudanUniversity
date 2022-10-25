# python 3.8.13
# CubicSplineInterpolation.py

# Created on Oct 18 16:02:04 2022
# @author: yinchaoyang
# --- utf-8 ---

# Use the Cubic Spline Interpolation Method
# to interpolate the function with the given points.

import numpy as np


def cubicSpine(points_x, points_y):
    n = len(points_x)
    
    matrix_A = np.zeros((n, n))
    matrix_A[0][0] = 1
    matrix_A[-1][-1] = 1
    for i in range(n - 2):
        matrix_A[i + 1][i] = points_x[i + 1] - points_x[i]
        matrix_A[i + 1][i + 1] = (points_x[i + 2] - points_x[i]) * 2
        matrix_A[i + 1][i + 2] = points_x[i + 2] - points_x[i + 1]
    
    matrix_B = np.zeros((n, 1))
    for i in range(n - 2):
        matrix_B[i + 1][0] = 6 / (points_x[i + 2] - points_x[i + 1]) * (points_y[i + 2] - points_y[i + 1]) + \
            6 / (points_x[i + 1] - points_x[i]) * (points_y[i] - points_y[i + 1])
    
    matrix_A_inv = np.linalg.inv(matrix_A)
    DD_function_x2 = matrix_A_inv @ matrix_B

    return DD_function_x2