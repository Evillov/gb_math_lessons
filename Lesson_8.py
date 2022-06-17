import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as splin

# import scipy.linalg

# 1. Решите линейную систему:
a_matrix = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]], float)
b_matrix = np.array([12, 2, 1], float)

x = np.linalg.solve(a_matrix, b_matrix)

print(f"1. Решите линейную систему \n Ответ:\n {x}")

# 2. Найдите псевдорешение:
# x + 2y – z = 1
# 3x – 4y = 7
# 8x – 5y + 2z = 12
# 2x – 5z = 7
# 11x +4y – 7z = 15

A_matrix = np.array([
    [1, 2, -1],
    [3, -4, 0],
    [8, -5, 2],
    [2, 0, -5],
    [11, 4, -7]
])

B_matrix = np.array([1, 7, 12, 7, 15])

print(f"2. Найдите псевдорешение \n"
      f"Ранг матрицы: {np.linalg.matrix_rank(A_matrix, 0.01)}")
x = np.linalg.lstsq(A_matrix, B_matrix, rcond=None)
print(x[0])

y = np.dot(A_matrix, x[0]) - B_matrix  # функция невязки

print(y)
print(f"Norm: {np.linalg.norm(y)}")

# 3 Сколько решений имеет линейная система:
print(f"3. Сколько решений имеет линейная система \n"
      f"[1, 2, 3]\n"
      f"[4, 5, 6]\n"
      f"[7, 8, 9]")

A_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]], float)

B_matrix = np.array(
    [12, 2, 1], float)

C_matrix = np.array([
    [1, 2, 3, 12],
    [4, 5, 6, 2],
    [7, 8, 9, 1], ], float)

print(f"Ранг исходной матрицы {np.linalg.matrix_rank(A_matrix, 0.01)}")  # Смотрим ранг исходной матрицы.
print(f"Ранг расширенной матрицы {np.linalg.matrix_rank(C_matrix, 0.01)}")  # Смотрим ранг расширенной матрицы.

print(
    f"{np.linalg.solve(A_matrix, B_matrix)} - Не решаемая система")  # не решаемая система, так как не совместная система.

B_matrix = np.array([0, 0, 0], float)  # пробуем с тривиальным решением х = 0, 0, 0 .
print(f"пробуем с тривиальным решением х = 0, 0, 0 \n {np.linalg.solve(A_matrix, B_matrix)}")

print("Попробуем с x = 1,1,1")  # пробуем с другим вариантом.

B_matrix = np.array([6, 15, 24], float)

print(np.linalg.solve(A_matrix, B_matrix))

print(np.dot(A_matrix, np.array([1, 1, 1], float)) - B_matrix)  # невязка

C_matrix = np.array([
    [1, 2, 3, 6],
    [4, 5, 6, 15],
    [7, 8, 9, 24]], float)

print(f"Ранг матрицы {np.linalg.matrix_rank(C_matrix, 0.01)}")

# 4. Считаем Low up разложение для матрицы
print(f"Считаем Low up разложение для матрицы:\n"
      f"[1, 2, 3]\n"
      f"[2, 16, 21]\n"
      f"[4, 28, 73]\n")
A_matrix = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]], float)
print(f"Проверяем определитель что он не равен \'0\' {np.linalg.det(A_matrix)}")

P, L, U = splin.lu(A_matrix)

# L * U * X = B.
# Решаем L * Y = B
# потом решаем U * X = Y
# придумаю например B = [4, 1, 8]

B_matrix = np.array([4, 1, 8], float)

Y_matrix = np.linalg.solve(L, B_matrix)

print("Наше уравнение: \n\tL * U * X = B")
print("Решаем L * Y = B")
print(Y_matrix)

print("Решаем U * X = Y")
print(np.linalg.solve(U, Y_matrix))

# 6.5 Найдите нормальное псевдорешение недоопределенной системы
# x + 2y – z = 1
# 8x – 5y + 2z = 12
print("6.5 Найдите нормальное псевдорешение недоопределенной системы:\n"
      "x + 2y – z = 1\n"
      "8x – 5y + 2z = 12\n")
A_matrix = np.array([[1, 2, -1], [8, -5, 2]], float)
B_matrix = np.array([1, 12], float)
print(np.linalg.lstsq(A_matrix, B_matrix, rcond=None)[0])

# 6.6 Найдите одно из псевдорешений вырожденной системы с помощью QR-разложения
print("6.6 Найдите одно из псевдорешений вырожденной системы с помощью QR-разложения")

A_matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]
                     ], float)

B_matrix = np.array([2, 5, 11], float)

Q, R = np.linalg.qr(A_matrix)
print(Q, "\n", R)
