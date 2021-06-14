import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = np.linalg.qr(A)
R_1 = R[:2, :2]
B_1 = np.dot(np.transpose(Q), B)[:2]
X_1 = np.linalg.solve(R_1, B_1)
X = np.append(X_1, 0)
print("Одно из псевдорешений СЛАУ:", X)
print("Норма: ", np.linalg.norm(X))
