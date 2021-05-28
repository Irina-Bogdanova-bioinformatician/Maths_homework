import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 21)
y1 = 3*x + 1
y2 = (-1/3)*x + 1
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()
