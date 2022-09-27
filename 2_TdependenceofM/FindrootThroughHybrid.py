# python 3.8.13
# FindrootThroughHybrid.py

# Created on Sep 24 17:30:36 2022
# @author: yinchaoyang
# --- utf-8 ---

# module for the main file Solve_and_Plot.py

import math

GOAL = 0
EPSILON = 1e-12

# set the initial value
a1 = 0
a2 = 1
a3 = 2

# --------------------------------------- #
# Compared to FindRoots\hybrid_method.py, #
# the parameter t needs to be received by #
# the functions as follows.               #
# --------------------------------------- #

def Function(t, x):
    return math.tanh(x / t) - x

def D_Function(t, x):
    return -1 + 1 / ((math.cosh(x/t))**2 * t)


def Bisection(t, a, b):
    x = (a + b) / 2
    if abs(Function(t, a) - GOAL) < EPSILON:
        return a
    elif abs(Function(t, b) - GOAL) < EPSILON:
        return b
    while abs(Function(t, x) - GOAL) >= EPSILON:
        x = (a + b) / 2
        if Function(t, x) * Function(t, a) < 0:
            b = x
        elif Function(t, x) * Function(t, b) < 0:
            a = x
    return x


def Hybrid(t, a, b):
    x = (a + b) / 2

    while abs(Function(t, x) - GOAL) >= EPSILON:
        if D_Function(t, x) != 0:
            x = x - Function(t, x) / D_Function(t, x)
            if a < x and x < b:
                if Function(t, x) * Function(t, a) < 0:
                    b = x
                elif Function(t, x) * Function(t, b) < 0:
                    a = x
            else:
                Bisection(t, a, b)
        else:
            Bisection(t, a, b)
        
    return x
