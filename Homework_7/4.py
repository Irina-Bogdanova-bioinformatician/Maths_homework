import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([1, 5], float)
b = np.array([2, 8], float)
X, Y = np.array([0, 0]), np.array([0, 0])
U, V = np.array([a[0], b[0]]), np.array([a[1], b[1]])
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
plt.xlim(-1, 3)
plt.ylim(-1, 10)
plt.grid(True)
alpha = np.pi / 2 - math.acos(2 / np.linalg.norm(b)) - math.acos(5 / np.linalg.norm(a))
scalar = np.linalg.norm(a) * np.linalg.norm(b) * math.cos(alpha)
print("Скалярное произведение векторов равно:", scalar)
plt.show()
