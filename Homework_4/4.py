import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0.0101, 0.0199, 98)
x_1 = np.pi / a
x_2 = []
x_3 = []
a_2 = []
a_3 = []
for i in a:
    x_2_checker = np.pi * 2 / i
    x_3_checker = np.pi * 3 / i
    if x_2_checker < 500:
        x_2.append(x_2_checker)
        a_2.append(i)
    if x_3_checker < 500:
        x_3.append(x_3_checker)
        a_3.append(i)
plt.plot(a, x_1)
plt.plot(a_2, x_2)
plt.plot(a_3, x_3)
plt.xlabel("a")
plt.ylabel("x")
plt.show()
