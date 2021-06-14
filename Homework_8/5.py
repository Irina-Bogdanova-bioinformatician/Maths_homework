import matplotlib.pyplot as plt
import numpy as np


def q(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


X = np.linspace(1.3, 1.5, 100)
plt.plot(X, q(X, 10 * X - 14, 21 * X - 29))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
