import numpy as np


""" Представленная в задаче СЛАУ не имеет решений (ранг расширенной матрицы больше ранга исходной).
    Изменяем вектор правой части (B) так, чтобы система стала совместной, и решаем ее.
"""

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12, 2, 1]])
C = np.concatenate((A, B.T), axis=1)
print(f"Ранг исходной матрицы: {np.linalg.matrix_rank(A, 0.0001)}, "
      f"ранг расширенной: {np.linalg.matrix_rank(C, 0.0001)}.")
B_new = np.array([[3, 6, 9]])
C_new = np.concatenate((A, B_new.T), axis=1)
print(f"Ранг исходной матрицы: {np.linalg.matrix_rank(A, 0.0001)}, "
      f"ранг расширенной (новой): {np.linalg.matrix_rank(C_new, 0.0001)}.")
if np.linalg.matrix_rank(A, 0.0001) == np.linalg.matrix_rank(C_new, 0.0001):
    print(f"Если вектор В = {B_new}, ранги исходной и расширенной матриц равны, и СЛАУ имеет "
          f"бесконечное множество решений.")
