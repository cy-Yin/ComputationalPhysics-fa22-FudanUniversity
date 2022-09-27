# python 3.8.13
# bisection_method.py

# Created on Sep 22 15:20:24 2022
# @author: yinchaoyang
# version: 1.0
# --- utf-8 ---

# Find the 2 positive roots of x^3-5*x+3=0 through the bisection method.

EPSILON = 1e-5

# set the initial value
# the 2 roots are bracketed by (0, 1) and (1, 2)
a1 = 0
a2 = 1
a3 = 2

def Function(x):
    return x**3 - 5 * x + 3


def Bisection(a, b):
    while b - a >= EPSILON:
        x = (a + b) / 2
        if Function(x) * Function(a) < 0:
            b = x
        elif Function(x) * Function(b) < 0:
            a = x
        
    return x

if __name__ == '__main__':
    print("Find the 2 positive roots of x^3-5*x+3=0 through the bisection method.")
    print("root1 = %.4f" % Bisection(a1, a2))
    print("root2 = %.4f" % Bisection(a2, a3))