import matplotlib.pyplot as plt
import math
import numpy as np

x_1 = []
x_2 = []
y_1 = []
y_2 = []
y_3 = []
y_4 = []
a = float(input("Введите значение показателя a (1/2 действительной оси гиперболы): "))
b = float(input("Введите значение показателя b (1/2 мнимой оси гиперболы): "))
for i in np.arange(-a - 10, -a + 0.01, 0.01):
    if i <= a:
        x_1.append(i)
        y_1.append(math.sqrt(i ** 2 * b ** 2 / a ** 2 - b ** 2))
        y_2.append(- math.sqrt(i ** 2 * b ** 2 / a ** 2 - b ** 2))
    else:
        x_1.append(a)
        y_1.append(0)
        y_2.append(0)
for i in np.arange(a, a + 10, 0.01):
    x_2.append(i)
    y_3.append(math.sqrt(i ** 2 * b ** 2 / a ** 2 - b ** 2))
    y_4.append(- math.sqrt(i ** 2 * b ** 2 / a ** 2 - b ** 2))
plt.plot(x_1, y_1, color="magenta")
plt.plot(x_1, y_2, color="magenta")
plt.plot(x_2, y_3, color="magenta")
plt.plot(x_2, y_4, color="magenta")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()
