import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
plt.plot(x, 2*np.cos(x - 3) + 4)
plt.plot(x, 5*np.cos(x - 1) + 7, color="green")
plt.plot(x, -4*np.cos(x + 4) + 2, color="crimson")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
