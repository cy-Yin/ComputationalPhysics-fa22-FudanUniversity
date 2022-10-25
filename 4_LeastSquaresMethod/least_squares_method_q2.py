# python 3.8.13
# least_squares_method_q2.py

# Created on Oct 15 11:25:30 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# Using the T-X data to obtain constant a, b and c 
# with the least-squares "parabolic-line fitting" method.

import numpy as np
import matplotlib.pyplot as plt


T = np.array([14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9])
X = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

def parabolic_fitting(T, X):

    matrixA = np.array([
        len(X),    sum(X),    sum(X**2),
        sum(X),    sum(X**2), sum(X**3),
        sum(X**2), sum(X**3), sum(X**4),
    ]).reshape((3, 3))
    matrixB = np.array([
        sum(T),
        sum(T * X),
        sum(T * (X**2)),
    ]).reshape((3, 1))

    u, s, v_T = np.linalg.svd(matrixA)
    s = np.diag(s)
    s_inv = np.linalg.inv(s)

    x = v_T.T @ s_inv @ (u.T) @ matrixB

    a = float(x[0])
    b = float(x[1])
    c = float(x[2])
    return a, b, c

if __name__ == '__main__':
    a, b, c = parabolic_fitting(T, X)
    print("a =", a)
    print('b =', b)
    print("c =", c)

    # Plot the result.
    x1 = X
    y1 = T
    plt.plot(x1, y1, 'or', label="data points")
    x2 = np.linspace(X[0], X[-1], 200)
    y2 = (a + b * x2 + c * x2**2)
    plt.plot(x2, y2, 'b', label="fitting function", alpha=0.6)
    plt.xlabel("$x$ / cm")
    plt.ylabel("$T$")
    plt.legend(loc="best")
    plt.show()