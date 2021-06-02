import numpy as np
import matplotlib.pyplot as plt

""" Создаем список из 10 массивов, содержащих по 10 рандомных чисел (из заданного интервала). 
    Затем находим сумму чисел в каждом массиве, внося значение суммы в новый список.
"""

new_list = []
sum_list = []
for i in range(0, 10):
    new_list.append(np.random.randint(0, 10, 10))
for el in new_list:
    sum_list.append(np.sum(el))
print(sum_list)
num_bins = 5
n, bins, patches = plt.hist(sum_list, num_bins)
plt.xlabel("x")
plt.ylabel("Probability")
plt.title("Histogram")
plt.show()
