import matplotlib.pyplot as plt
import math
import numpy as np

x = []
y_circle_1 = []
y_circle_2 = []
R = float(input("Введите радиус окружности "))
list_1 = input("Введите координаты центра окружности (x0, y0) через запятую ").split(",")
list_1_modified = [int(i) for i in list_1]
a, b = list_1_modified
for i in np.arange(a - R, a + R + 0.01, 0.01):
    if i <= (a + R):
        x.append(i)
        y_circle_1.append(math.sqrt(R**2 - (i - a)**2) + b)
        y_circle_2.append(-(math.sqrt(R**2 - (i - a)**2)) + b)
    else:
        x.append(a + R)
        y_circle_1.append(b)
        y_circle_2.append(b)
plt.plot(x, y_circle_1, color="indigo")
plt.plot(x, y_circle_2, color="indigo")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()
