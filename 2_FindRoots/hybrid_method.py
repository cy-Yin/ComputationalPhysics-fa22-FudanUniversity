# python 3.8.13
# hybrid_method.py

# Created on Sep 22 15:34:56 2022
# @author: yinchaoyang
# version: 1.0
# --- utf-8 ---

# Find the 2 positive roots of x^3-5*x+3=0 through the hybrid method.

GOAL = 0
EPSILON = 1e-14

# set the initial value
a1 = 0
a2 = 1
a3 = 2

def Function(x):
    return x**3 - 5 * x + 3

def D_Function(x):
    return 3 * x**2 - 5


def Bisection(a, b):
    while b - a >= EPSILON:
        x = (a + b) / 2
        if Function(x) * Function(a) < 0:
            b = x
        elif Function(x) * Function(b) < 0:
            a = x
    return x


def Hybrid(a, b):
    x = (a + b) / 2

    while b - a >= EPSILON:
        if D_Function(x) != 0:
            x0 = x
            x = x - Function(x) / D_Function(x)
            if abs(x0 - x) < EPSILON:
                return x
            if a < x and x < b:
                if Function(x) * Function(a) < 0:
                    b = x
                elif Function(x) * Function(b) < 0:
                    a = x
            else:
                Bisection(a, b)
        else:
            Bisection(a, b)
        
    return x

if __name__ == '__main__':
    print("Find the 2 positive roots of x^3-5*x+3=0 through the hybrid method.")
    print("root1 = %.14f" % Hybrid(a1, a2))
    print("root2 = %.14f" % Hybrid(a2, a3))
