# Задание 4. Рекурсивная проверка палиндрома.
def is_palindrome(text, left=0, right=None):
    if right is None:
        right = len(text) - 1
    # Если дошли до середины, все пары символов совпали.
    if left >= right:
        return True
    # Сравниваем символы с двух концов строки.
    if text[left] != text[right]:
        return False
    # Переходим к следующей паре, сдвигаясь к середине.
    return is_palindrome(text, left + 1, right - 1)


print("=" * 60)
print("Задание 4. Проверка палиндрома")
print("\n--- ВВОД ДАННЫХ ---")
print("Пробелы, регистр букв и знаки препинания учитываются.")
text = input("Введите строку: ")

print("\n--- РЕЗУЛЬТАТ ---")
if is_palindrome(text):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
print("=" * 60)
