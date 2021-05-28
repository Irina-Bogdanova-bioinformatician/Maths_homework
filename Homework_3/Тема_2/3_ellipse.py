import matplotlib.pyplot as plt
import math
import numpy as np

x = []
y_1 = []
y_2 = []
a = float(input("Введите значение показателя a (1/2 большой оси эллипса): "))
b = float(input("Введите значение показателя b (1/2 малой оси эллипса): "))
for i in np.arange(-a, a + 0.01, 0.01):
    if i <= a:
        x.append(i)
        y_1.append(math.sqrt(b**2 - i**2 * b**2 / a**2))
        y_2.append(- math.sqrt(b**2 - i**2 * b**2 / a**2))
    else:
        x.append(a)
        y_1.append(0)
        y_2.append(0)
plt.plot(x, y_1, color="navy")
plt.plot(x, y_2, color="navy")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()
