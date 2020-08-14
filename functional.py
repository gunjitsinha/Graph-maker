'''
author = @gunjitsinha
'''

import matplotlib.pyplot as plt
import numpy as np

def formalities():
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    
def exponential():
    x = np.arange(0, 20, 0.1)
    y = 2**x
    plt.plot(x, y)
    plt.title('Exponential')
    formalities()

def logarithamic():
    x = np.arange(-100, 100, 0.1)
    y = np.log(x)
    plt.plot(x, y)
    plt.title('Logarithamic')
    formalities()





