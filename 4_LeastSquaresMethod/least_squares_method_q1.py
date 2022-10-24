# python 3.8.13
# least_squares_method_version1.py

# Created on Oct 15 09:34:06 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Using the P-V data to obtain constant a and b 
# with the least-squares "linear fitting" method.

import numpy as np
import matplotlib.pyplot as plt


T = [14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9]
X = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

def linear_fitting(T, X):
    n = len(T) # the total number of the points

    C = [0, 0, 0, 0]
    for i in range(n):
        C[0] += X[i]        # c0 = \sum(x_i)
        C[1] += X[i] ** 2   # c1 = \sum((x_i)^2)
        C[2] += T[i]        # c2 = \sum(y_i)
        C[3] += X[i] * T[i] # c3 = \sum(x_i * y_i)

    a = (C[0] * C[3] - C[1] * C[2]) / (C[0] * C[0] - n * C[1])
    b = (C[0] * C[2] - n * C[3]) / (C[0] * C[0] - n * C[1])
    
    return a, b

if __name__ == '__main__':
    a, b = linear_fitting(T, X)
    
    print("a =", a)
    print('b =', b)

    # Plot the result.
    x1 = X
    y1 = T
    plt.plot(x1, y1, 'or', label="data points")
    x2 = np.linspace(X[0], X[-1], 200)
    y2 = (a + b * x2)
    plt.plot(x2, y2, 'b', label="fitting function", alpha=0.6)
    plt.xlabel("$x$ / cm")
    plt.ylabel("$T$")
    plt.legend(loc="best")
    plt.show()