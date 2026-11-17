# Задание 7. Рекурсивное разложение на сумму простых чисел.
def is_prime(number):
    if number < 2:
        return False
    # У простого числа нет делителей от 2 до квадратного корня из числа.
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def prime_sum(number):
    # Если число простое, оно само является готовым разложением.
    if is_prime(number):
        return [number]
    if number < 2:
        return None
    # Пробуем вычесть простое число и рекурсивно разложить остаток.
    for prime in range(2, number):
        if is_prime(prime):
            rest = prime_sum(number - prime)
            if rest is not None:
                return [prime] + rest
    return None


print("=" * 60)
print("Задание 7. Разложение на сумму простых чисел")
print("\n--- ВВОД ДАННЫХ ---")
n = int(input("Введите целое число не меньше 2: "))

print("\n--- РЕЗУЛЬТАТ ---")
if n < 2:
    print("Ошибка: число должно быть не меньше 2.")
else:
    # Выводим одно подходящее разложение. Простые слагаемые могут повторяться.
    parts = prime_sum(n)
    print(f"{n} = " + " + ".join(map(str, parts)))
print("=" * 60)
