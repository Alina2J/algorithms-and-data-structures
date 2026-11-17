# Задание 6. Обмен минимума и максимума в каждой строке.
def read_size(prompt):
    # Повторяем ввод, пока не получим положительное целое число.
    while True:
        try:
            size = int(input(prompt))
            if size > 0:
                return size
            print("Размер должен быть положительным.")
        except ValueError:
            print("Введите одно целое число, например 3.")


def read_matrix(m, n):
    # Внешний список хранит строки, каждая строка — отдельный список чисел.
    matrix = []
    print(f"Введите матрицу построчно: {m} строк, по {n} чисел через пробел.")
    for i in range(m):
        while True:
            try:
                # split разделяет строку по пробелам, map переводит части в числа.
                row = list(map(float, input(f"Строка {i + 1}: ").split()))
            except ValueError:
                print("Введите  числа через пробел.")
                continue
            if len(row) != n:
                print(f"Нужно ровно {n} чисел. Сейчас введено: {len(row)}.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix):
    # Одинаковая ширина полей помогает видеть столбцы при выводе.
    for row in matrix:
        print(" ".join(f"{value:10g}" for value in row))


print("=" * 60)
print("Задание 6. Обмен минимума и максимума в каждой строке")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
for i in range(m):
    min_index = 0
    max_index = 0
    # Запоминаем индексы, чтобы затем обменять именно элементы текущей строки.
    for j in range(1, n):
        if matrix[i][j] < matrix[i][min_index]:
            min_index = j
        if matrix[i][j] > matrix[i][max_index]:
            max_index = j
    # Одновременное присваивание меняет два значения местами.
    matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]
print("Матрица после обмена минимума и максимума в каждой строке:")
print_matrix(matrix)
print("=" * 60)
