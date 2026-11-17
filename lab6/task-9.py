# Задание 9. Сортировка строк по первому элементу.
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
print("Задание 9. Сортировка строк по первому элементу")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
# Сортировка вставками: очередную строку ставим на место среди уже упорядоченных.
# Перемещаем строки целиком, сохраняя порядок элементов внутри каждой строки.
for i in range(1, m):
    current_row = matrix[i]
    j = i - 1
    while j >= 0 and matrix[j][0] > current_row[0]:
        matrix[j + 1] = matrix[j]
        j -= 1
    matrix[j + 1] = current_row
print("Строки упорядочены по возрастанию первых элементов.")
print("При одинаковых первых элементах сохранён исходный порядок строк.")
print_matrix(matrix)
print("=" * 60)
