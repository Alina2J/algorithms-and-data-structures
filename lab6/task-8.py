# Задание 8. Обмен левой верхней и правой нижней четвертей.
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
print("Задание 8. Обмен левой верхней и правой нижней четвертей")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите чётное количество строк M: ")
n = read_size("Введите чётное количество столбцов N: ")
while m % 2 != 0 or n % 2 != 0:
    print("Оба размера должны быть чётными.")
    m = read_size("Введите чётное количество строк M: ")
    n = read_size("Введите чётное количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
half_m = m // 2
half_n = n // 2
# Перебираем только левую верхнюю четверть.
# Парный элемент справа внизу смещён на половину высоты и ширины матрицы.
for i in range(half_m):
    for j in range(half_n):
        matrix[i][j], matrix[i + half_m][j + half_n] = matrix[i + half_m][j + half_n], matrix[i][j]
print("Матрица после обмена четвертей:")
print_matrix(matrix)
print("=" * 60)
