import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
k1 = 1
k2 = 3
plt.plot(x, np.cos(k1 * x))
plt.plot(x, np.cos(k2 * x))
plt.show()
