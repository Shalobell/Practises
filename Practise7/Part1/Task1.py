import numpy as np


vector = np.array([4,6,3,23,56,1,9,8])

print("Исходный вектор:")
print(vector)


indices = np.array([0, 2, 4, 6])
indexed_elements = vector[indices]
print("1. Индексация по элементам (5 значений):")
print(f"Индексы: {indices}")
print(f"Элементы: {indexed_elements}")

range_slice = vector[2:7]
print("2. Индексация по диапазону [2:7]:")
print(range_slice)

reversed_vector = vector[::-1]
print("3. Перевернутый массив:")
print(reversed_vector)

vector_copy = vector.copy()
vector_copy[3] = 100
print("4. Операция присвоения (vector[3] = 100):")
print(f"Исходный: {vector}")
print(f"После присвоения: {vector_copy}")

multiplied = vector * 2
print("5. Математическая операция умножения:")
print(multiplied)

another_vector = np.array([1, 2, 3, 4, 5, 6, 7, 8])
multiplied_vectors = vector * another_vector
print("5. Умножение на другой вектор:")
print(f"vector * {another_vector} = {multiplied_vectors}")


max_index = np.argmax(vector)
min_index = np.argmin(vector)
print("6. Argmax и argmin:")
print(f"Индекс максимального элемента (argmax): {max_index}, значение: {vector[max_index]}")
print(f"Индекс минимального элемента (argmin): {min_index}, значение: {vector[min_index]}")

appended_vector = np.append(vector, [99, 88, 77])
print("7. Метод append:")
print(f"Исходный вектор: {vector}")
print(f"После append: {appended_vector}")