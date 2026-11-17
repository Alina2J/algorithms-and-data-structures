# Задание 6. Обратный порядок слов с помощью рекурсии.
def reverse_words(words, index=0):
    # Когда слова закончились, возвращаем пустой список.
    if index == len(words):
        return []
    # Сначала разворачиваем оставшиеся слова, затем добавляем текущее в конец.
    return reverse_words(words, index + 1) + [words[index]]


print("=" * 60)
print("Задание 6. Обратный порядок слов")
print("\n--- ВВОД ДАННЫХ ---")
text = input("Введите строку: ")

# split выделяет слова, а join соединяет их одним пробелом.
words = text.split()
result = " ".join(reverse_words(words))

print("\n--- РЕЗУЛЬТАТ ---")
print("Строка с обратным порядком слов:", result)
print("=" * 60)
