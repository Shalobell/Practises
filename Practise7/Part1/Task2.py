import numpy as np

matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
])

print("Исходная матрица 5x7:")
print(matrix)

dimension = matrix.ndim
print(f"1. Размерность матрицы (ndim): {dimension}")


shape = matrix.shape
print(f"2. Размерность объектов (shape): {shape}")
print(f"   Количество строк: {shape[0]}")
print(f"   Количество столбцов: {shape[1]}")


column_0 = matrix[:, 0]
column_1 = matrix[:, 1]
column_2 = matrix[:, 2]
column_3 = matrix[:, 3]
column_4 = matrix[:, 4]


print("3. Индексация по колонкам матрицы:")
print(f"Колонка 0: {column_0}")
print(f"Колонка 1: {column_1}")
print(f"Колонка 2: {column_2}")
print(f"Колонка 3: {column_3}")
print(f"Колонка 4: {column_4}")


columns_1_3 = matrix[:, [1, 3]]
print("Колонки 1 и 3:")
print(columns_1_3)

print("4. Поэлементное сложение:")

# Матричное сложение
sum_matrix = matrix + matrix
print("Результат сложения матрицы самой с собой (matrix + matrix):")
print(sum_matrix)

# Сложение со скаляром
scalar_sum = matrix + 10
print("Сложение исходной матрицы со скаляром (matrix + 10):")
print(scalar_sum)


transposed_matrix = matrix.transpose()
print("5. Транспонированная матрица (transpose):")
print("Исходная матрица (5x7):")
print(matrix)
print("Транспонированная матрица (7x5):")
print(transposed_matrix)
print(f"Размерность исходной: {matrix.shape}")
print(f"Размерность транспонированной: {transposed_matrix.shape}")