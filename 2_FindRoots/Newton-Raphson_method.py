# python 3.8.13
# Newton-Raphson_method.py

# Created on Sep 22 15:26:40 2022
# @author: yinchaoyang
# version: 1.0
# --- utf-8 ---

# Find the 2 positive roots of x^3-5*x+3=0 through the Newton-Raphson method.

EPSILON = 1e-14

# inherit the value from bisection_method.py
# set as the 2 initial values.
x1 = 0.6566
x2 = 1.8342

def Function(x):
    return x**3 - 5 * x + 3

def D_Function(x):
    return 3 * x**2 - 5

def NewtonRaphson(x):
    x0 = x
    x = x - Function(x) / D_Function(x)
    while abs(x - x0) >= EPSILON:
        x0 = x
        x = x - Function(x) / D_Function(x)
    return x


if __name__ == '__main__':
    print("Find the 2 positive roots of x^3-5*x+3=0 through the NewtonRaphson method.")
    print("root1 = %.14f" % NewtonRaphson(x1))
    print("root2 = %.14f" % NewtonRaphson(x2))