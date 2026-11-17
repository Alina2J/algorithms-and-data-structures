# Задание 4. Количество элементов выше среднего в каждом столбце.
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
print("Задание 4. Количество элементов выше среднего в каждом столбце")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
counts = []
for j in range(n):
    # Фиксируем столбец j и перебираем все его строки.
    total = 0.0
    for i in range(m):
        total += matrix[i][j]
    average = total / m
    count = 0
    # После вычисления среднего ещё раз проходим по этому столбцу.
    for i in range(m):
        if matrix[i][j] > average:
            count += 1
    counts.append(count)
    print(f"Столбец {j + 1}: среднее = {average:g}, элементов выше среднего = {count}")
print("=" * 60)
