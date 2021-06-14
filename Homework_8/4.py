import numpy as np
import scipy.linalg

A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)
print("Матрица Р:\n", P)
print("Матрица L:\n", L)
print("Матрица U:\n", U)
B = np.array([[3, 21, 73]])
C = np.concatenate((A, B.T), axis=1)
print(f"Ранг исходной матрицы: {np.linalg.matrix_rank(A, 0.0001)}, "
      f"ранг расширенной: {np.linalg.matrix_rank(C, 0.0001)}.")
B_2 = np.array([3, 21, 73])
X = np.linalg.lstsq(A, B_2, rcond=None)
print("Решение СЛАУ, если вектор правых частей равен (3, 21, 73):", X[0])
