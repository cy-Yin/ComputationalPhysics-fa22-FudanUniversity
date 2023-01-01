import numpy as np
import matplotlib.pyplot as plt

def uniform_distribution_on_a_3D_sphere(num):
    u = np.random.rand(num)
    v = np.random.rand(num)
    theta = 2 * np.pi * u
    phi = np.arccos(2*v-1)
    x = np.sin(theta) * np.sin(phi)
    y = np.cos(theta) * np.sin(phi)
    z = np.cos(phi)
    
    return x, y, z

def plot(x, y, z):
    ax = plt.axes(projection='3d')
    ax.scatter(x,y,z, 'o', s=1)
    ax.set_xlabel('X Axes')
    ax.set_ylabel('Y Axes')
    ax.set_zlabel('Z Axes')
    plt.show()

if __name__ == '__main__':
    number = 10000
    x, y, z = uniform_distribution_on_a_3D_sphere(number)
    plot(x, y, z)