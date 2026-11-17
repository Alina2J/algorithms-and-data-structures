# Задание 5. Рекурсивный бинарный поиск.
def binary_search(numbers, target, left, right):
    # Границы пересеклись — подходящего элемента нет.
    if left > right:
        return -1
    middle = (left + right) // 2
    if numbers[middle] == target:
        return middle
    # В отсортированном массиве достаточно искать только в одной половине.
    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)
    return binary_search(numbers, target, middle + 1, right)


print("=" * 60)
print("Задание 5. Бинарный поиск")
print("\n--- ВВОД ДАННЫХ ---")
# split разбивает строку по пробелам, int превращает каждую часть в целое число.
numbers = list(map(int, input("Введите целые числа по возрастанию через пробел: ").split()))
target = int(input("Введите искомое число: "))

print("\n--- РЕЗУЛЬТАТ ---")
# Повторяющиеся числа допускаются, но порядок должен быть неубывающим.
if numbers != sorted(numbers):
    print("Ошибка: числа должны быть отсортированы по возрастанию.")
else:
    index = binary_search(numbers, target, 0, len(numbers) - 1)
    if index == -1:
        print("Число не найдено.")
    else:
        print("Индекс найденного элемента (с нуля):", index)
        print("Позиция элемента (с единицы):", index + 1)
print("=" * 60)
