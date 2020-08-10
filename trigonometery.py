import matplotlib.pyplot as plt
import numpy as np

def sine():
    x = np.arange(-10, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Sin')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()

def cosine():
    x = np.arange(-10, 10, 0.1)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('Cos')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()

def tangent():
    x = np.arange(-2*np.pi, 2*np.pi, 0.1)
    y = np.tan(x)
    y[:-1][np.diff(y) < 0] = np.nan
    plt.ylim(-3, 3)
    plt.plot(x,y)
    plt.title('Tan')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()

def cotangent():
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
    y = 1/(np.tan(x))
    y[:-1][np.diff(y) > 0] = np.nan
    plt.ylim(-3, 3)
    plt.plot(x, y)
    plt.title('Cot')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()




