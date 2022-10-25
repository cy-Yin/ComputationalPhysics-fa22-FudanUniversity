# python 3.8.13
# NewtonInterpolation.py

# Created on Oct 17 21:34:54 2022
# @author: yinchaoyang
# --- utf-8 ---

# Use the Newton Interpolation Method
# to interpolate the function with the given points.

import numpy as np

def cal_parameters(points_x, points_y): 
    # Calculate the parameters of the normal newton interpolation function.
    # b_i, 0 <= i <= n
    parameters = np.zeros((len(points_x), len(points_x)))
    for i in range(len(points_y)):
        parameters[i][0] = points_y[i]

    # f[x_j, x_j-1, ... , x_i] = (f[x_j, x_j-1, ... , x_i+1] - f[x_j-1, x_j-2, ... , x_i]) / (x_j - x_i)
    for column in range(1, len(points_x)):
        for row in range(len(points_x) - column):
            parameters[row][column] = (parameters[row][column - 1] - \
                parameters[row + 1][column - 1]) / (points_x[row] - points_x[row + column])

    return parameters


def newtonInterpolation(points_x, points_y, x):
    parameters = cal_parameters(points_x, points_y)

    # Print the normal function of newton interpolation.
    print("The newton Interpolation function is")
    print(" " * 3, end='')
    for i in range(len(points_x)):
        print("%.6f" % parameters[0][i], end='')
        if i == 0:
            pass
        else:
            for j in range(i):
                print(" * (x - (%.4f))" % points_x[j], end='')
        if i != len(points_x) - 1:
            print("\n + ", end='')

    # calculate the values of y of the given x
    y = np.zeros(x.shape)
    for i in range(len(points_x)):
        par = parameters[0][i]
        func = np.ones(x.shape)
        for j in range(i):
            func = func * (x - points_x[j])
        
        y += par * func

    return y