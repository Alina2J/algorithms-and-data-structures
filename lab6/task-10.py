# Задание 10. Суммы диагоналей, параллельных главной.
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
print("Задание 10. Суммы диагоналей, параллельных главной")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите порядок квадратной матрицы M: ")
n = m
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
diagonal_sums = []
# На каждой такой диагонали разность j - i постоянна.
# Начинаем с правого верхнего угла, затем идём к главной диагонали и ниже неё.
for offset in range(m - 1, -m, -1):
    total = 0.0
    # Выбираем первую строку диагонали: сверху или с левого края.
    i = max(0, -offset)
    j = i + offset
    start_row, start_column = i + 1, j + 1
    while i < m and j < m:
        total += matrix[i][j]
        i += 1
        j += 1
    diagonal_sums.append(total)
    print(f"Диагональ от ({start_row}, {start_column}): сумма = {total:g}")
print("=" * 60)
