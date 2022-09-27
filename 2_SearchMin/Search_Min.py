import math

EPSILON = 1e-10

def Function(x, y): # 原函数
    result = math.sin(x + y) + math.cos(x + 2 * y)
    return result

def D_Function_x(x, y): # x方向上的偏导数
    Partial_x_result = math.cos(x + y) - math.sin(x + 2 * y)
    return Partial_x_result

def D_Function_y(x, y): # y方向上的偏导数
    Partial_y_result = math.cos(x + y) - 2 * math.sin(x + 2 * y)
    return Partial_y_result

print("Please input the initial point (x, y):")
x = float(input("x = "))
y = float(input("y = "))

# 最速下降法求函数极值（最值）
def Steepest_descent(x, y):
    a = 0.05 # 权重参数
    x0 = x
    y0 = y
    x = x - a * D_Function_x(x, y) # x方向的迭代公式
    y = y - a * D_Function_y(x, y) # y方向的迭代公式
    count = 0 # 迭代次数
    while max(abs(x - x0), abs(y - y0)) >= EPSILON and count < 1e6:
        x0 = x
        y0 = y
        x = x - a * D_Function_x(x, y)
        y = y - a * D_Function_y(x, y)
        count = count + 1
    
    return x, y

xOfMin, yOfMin = Steepest_descent(x, y)
print("The minimum of the function is ", Function(xOfMin, yOfMin))