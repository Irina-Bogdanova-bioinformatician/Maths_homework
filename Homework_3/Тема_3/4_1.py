from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
plt.plot(x, (np.exp(x) - 1 + x) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('scaled')
plt.show()


def equations(p):
    x_new, y_new = p
    return y_new - x_new ** 2 + 1, np.exp(x_new) + x_new * (1 - y_new) - 1


x1, y1 = fsolve(equations, (-2, 1))
x2, y2 = fsolve(equations, (2, 4))
print(x1, y1)
print(x2, y2)
