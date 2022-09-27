import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**2 + x +1

N = 40 #amostras
x = 5*np.random.rand(N,1)

y = f(x)

plt.plot(x,y,"*")
plt.show()