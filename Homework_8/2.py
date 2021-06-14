import numpy as np

A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
a = np.linalg.lstsq(A, B, rcond=None)
print(a)
checking = None
for i, el in enumerate(a):
    if i == 0:
        print("Псевдорешением СЛАУ является:", el)
        checking = np.dot(A, el)
    elif i == 1:
        print("Сумма квадратов невязок:", el)
    elif i == 2:
        print("Ранг матрицы A:", el)
print("Проверяем найденные решения, подставив их в уравнения. Получаем следующую матрицу В:", checking)
