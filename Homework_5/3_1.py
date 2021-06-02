import numpy as np

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
probability_calc = 6 * 0.5**2 * 0.5**2
print(f"Вероятность выпадения двух успехов при четырех испытаниях (метод Монте-Карло): {k / n}")
print(f"Вероятность выпадения двух успехов при четырех испытаниях (формула Бернулли): {probability_calc}")
