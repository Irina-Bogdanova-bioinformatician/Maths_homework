import numpy as np
import matplotlib.pyplot as plt

""" Создаем список из 10 рандомных чисел (из заданного интервала), затем с помощью цикла создаем еще 9 списков,
    сразу складывая числа попарно (x0 + x0, x1 + x1... x9 + x9)
"""

new_list = []
sum_list = np.random.randint(0, 10, 10)
for i in range(0, 9):
    sum_list = sum_list + np.random.randint(0, 10, 10)
print(sum_list)
num_bins = 5
n, bins, patches = plt.hist(sum_list, num_bins)
plt.xlabel("x")
plt.ylabel("Probability")
plt.title("Histogram")
plt.show()
