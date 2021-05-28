from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z_1 = 2 * X + 5 * Y
Z_2 = 2 * X + 5 * Y + 30
ax.plot_wireframe(X, Y, Z_1, color="blue")
ax.plot_wireframe(X, Y, Z_2, color="red")
show()
