from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = figure()
ax = Axes3D(fig)
X_1 = np.arange(-50, 50, 1)
Y_1 = np.arange(-50, 50, 1)
X_1, Y_1 = np.meshgrid(X_1, Y_1)
Z_1 = X_1**2 / 25 + Y_1**2 / 16
X_2 = np.arange(-30, 30 + 0.1, 0.1)
Y_2 = np.arange(-20, 20 + 0.1, 0.1)
X_2, Y_2 = np.meshgrid(X_2, Y_2)
Z_2 = np.sqrt(400 - (400*(X_2**2 / 900)) - (Y_2**2))
Z_3 = - np.sqrt(400 - (400*(X_2**2 / 900)) - (Y_2**2))
ax.plot_wireframe(X_1, Y_1, Z_1, color="blue")
ax.plot_wireframe(X_2, Y_2, Z_2, color="red")
ax.plot_wireframe(X_2, Y_2, Z_3, color="green")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylabel('z')
show()
