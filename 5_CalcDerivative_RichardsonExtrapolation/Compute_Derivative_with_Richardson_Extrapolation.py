# python 3.8.13
# Compute_Derivative_with_Richardson_Extrapolation.py

# Created on Oct 27 22:12:32 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# ------------------ description of problem ------------------ #
# Compute the derivative of f(x) = sin(x) at x = pi/3 
# using the Richardson extrapolation algorithm
# Start with h = 1 
# Find the number of rows in the Richardson table required to
# estimate the derivative with six significant decimal digits
# Output the Richardson table.
# ------------------------------------------------------------ #

import numpy as np

# Constants
Error = 1e-6
x0 = np.pi / 3
h = 1

def function(x): # f(x) = sin(x)
    return np.sin(x)

def D_Function(x): # f'(x) = cos(x)
    return np.cos(x)

def phi(x0, h):
    return 1 / (2 * h) * (function(x0 + h) - function(x0 - h))

# Richardson extrapolation algorithm
def RichardsonExtrapolation(num, x0, h):
    RichardsonTable = np.zeros((num, num))

    for row in range(num): # D(n, 0) = \phi( h / 2^n)
        RichardsonTable[row][0] = phi(x0, h / (2**row))

    for n in range(1, num):
        for m in range(1, n + 1):
            RichardsonTable[n][m] = RichardsonTable[n][m - 1] + 1 / (4**m - 1) * \
                (RichardsonTable[n, m - 1] - RichardsonTable[n - 1, m - 1]) # recursion formula

    return RichardsonTable


if __name__ == '__main__':
    num = 1 # the number of rows in the Richardson table
    RichardsonTable = RichardsonExtrapolation(num, x0, h)
    if abs(RichardsonTable[num - 1][num - 1] - D_Function(x0)) < Error:
        pass
    else:
        num = num + 1
        RichardsonTable = RichardsonExtrapolation(num, x0, h)
        # Compare D(n, n) with D(n-1, n-1) to estimate the number of significant decimal digits 
        while abs(RichardsonTable[num - 1][num - 1] - RichardsonTable[num - 2][num - 2]) >= Error:
            num = num + 1
            RichardsonTable = RichardsonExtrapolation(num, x0, h)

    print("The number of rows in Richardson table required " 
        "to estimate the derivative with six significant decimal digits is %d" % num)
    print("The Richardson Table is")
    print(RichardsonTable)
