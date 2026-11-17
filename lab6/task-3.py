# Задание 3. Столбец с наименьшим произведением.
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
print("Задание 3. Столбец с наименьшим произведением")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
# Сначала считаем произведение первого столбца: с ним сравним остальные.
min_product = 1.0
for i in range(m):
    min_product *= matrix[i][0]
min_column = 0
for j in range(1, n):
    product = 1.0
    for i in range(m):
        product *= matrix[i][j]
    # При равенстве оставляем первый найденный столбец.
    if product < min_product:
        min_product = product
        min_column = j
print("Номер столбца:", min_column + 1)
print(f"Наименьшее произведение: {min_product:g}")
print("=" * 60)
