# Задание 1. Обход матрицы по спирали против часовой стрелки.
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
print("Задание 1. Обход матрицы по спирали против часовой стрелки")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите нечётный порядок матрицы M: ")
while m % 2 == 0:
    print("Порядок матрицы должен быть нечётным.")
    m = read_size("Введите нечётный порядок матрицы M: ")
n = m
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
# Четыре границы ограничивают ещё не пройденную часть матрицы.
top, bottom = 0, m - 1
left, right = 0, n - 1
spiral = []
while left <= right and top <= bottom:
    # Идём вниз по левому столбцу, затем исключаем его из дальнейшего обхода.
    for i in range(top, bottom + 1):
        spiral.append(matrix[i][left])
    left += 1
    # Идём вправо по нижней строке.
    for j in range(left, right + 1):
        spiral.append(matrix[bottom][j])
    bottom -= 1
    # Проверяем границы, чтобы не записать центральные элементы повторно.
    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][right])
        right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            spiral.append(matrix[top][j])
        top += 1
print("Элементы по спирали:")
print(" ".join(f"{value:g}" for value in spiral))
print("=" * 60)
