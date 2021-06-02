import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.9
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
A = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, y,  rcond=None)[0]
print(f"Коэффициенты регрессии a и b равны {a}, {b} соответственно.")
plt.plot([0, 1], [b, a + b])
c = np.corrcoef(x, y)
print("Коэффициенты корреляции равны: ", c)
x_new = [(i - sum(x) / 100) for i in x]
y_new = [(i - sum(y) / 100) for i in y]
numerator = sum([(e * d) for e, d in zip(x_new, y_new)])
denominator = np.sqrt(sum([f**2 for f in x_new]) * sum([g**2 for g in y_new]))
correlation_coefficient = numerator / denominator
print("Коэффициент корреляции, расчитанный по формуле, равен", correlation_coefficient)
plt.show()
