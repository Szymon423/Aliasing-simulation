import numpy as np
import matplotlib.pyplot as plt
# equation: f(x) = sin(n * x + m * pi/10), m = -M/2, ... , M/2, n = 3, 
# for M = 64





def genarateImage(path, M, _n):
    f = lambda x, n, m : np.sin(n * x + m * np.pi / 10.)

    X = np.linspace(0, 2*np.pi, 10000)
    Y = f(X, _n, M)

    plt.figure(figsize=(1, 1), dpi=256)
    plt.polar(X, Y)
    plt.grid(False)
    plt.box(False)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(path)
    plt.close()



X = np.arange(-32, 33)
i = 0
for x in X:
    path = "5n propeller\\" + str(i) + ".png"
    genarateImage(path, x, 5)
    i += 1