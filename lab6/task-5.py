# Задание 5. Первый столбец только с нечётными числами.
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
                row = list(map(int, input(f"Строка {i + 1}: ").split()))
            except ValueError:
                print("Введите целые числа через пробел.")
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
print("Задание 5. Первый столбец только с нечётными числами")
print("\n--- ВВОД ДАННЫХ ---")
m = read_size("Введите количество строк M: ")
n = read_size("Введите количество столбцов N: ")
matrix = read_matrix(m, n)

print("\n--- РЕЗУЛЬТАТ ---")
print("Исходная матрица:")
print_matrix(matrix)
print()
column_number = 0
for j in range(n):
    all_odd = True
    for i in range(m):
        # Остаток 0 при делении на 2 означает чётное число, включая ноль.
        if matrix[i][j] % 2 == 0:
            all_odd = False
            break
    if all_odd:
        column_number = j + 1
        # Столбцы проверяем слева направо, поэтому первый найденный и нужен.
        break
print("Номер первого столбца только с нечётными числами:", column_number)
print("=" * 60)
