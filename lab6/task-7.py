# Задание 7. Обмен столбцов с минимумом и максимумом матрицы.
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
print("Задание 7. Обмен столбцов с минимумом и максимумом матрицы")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
minimum = matrix[0][0]
maximum = matrix[0][0]
min_column = 0
max_column = 0
# Ищем крайние значения во всей матрице, просматривая строки сверху вниз.
for i in range(m):
    for j in range(n):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
            min_column = j
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            max_column = j
# Обмениваем выбранные столбцы: в каждой строке меняем соответствующие элементы.
for i in range(m):
    matrix[i][min_column], matrix[i][max_column] = matrix[i][max_column], matrix[i][min_column]
print(f"Поменяли местами столбцы {min_column + 1} и {max_column + 1}.")
print_matrix(matrix)
print("=" * 60)
