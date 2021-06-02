import numpy as np

new_dict = {i: 0 for i in range(0, 37)}
for el in range(0, 10000):
    x = np.random.randint(0, 37)
    new_dict[x] += 1
print(f"Количество выпадений каждого из чисел на рулетке (n = 10000): {new_dict}")
probability_sum = 0
for value in new_dict.values():
    probability_sum += value / 10000
print(f"Сумма вероятностей несовместных событий (вероятностей выпадения числа от 0 до 36 на рулетке) равна"
      f" {probability_sum}")
