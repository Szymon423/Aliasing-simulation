import numpy as np
import matplotlib.pyplot as plt
# equation: f(x) = sin(n * x + m * pi/10), m = -M/2, ... , M/2, n = 3, 
# for M = 64


M = 64
f = lambda x, n, m : np.sin(n * x + m * np.pi / 10.)

X = np.linspace(0, 2*np.pi, 1000)

Y = f(X, 3, -32)

plt.figure()
plt.polar(X, Y)
plt.show()
