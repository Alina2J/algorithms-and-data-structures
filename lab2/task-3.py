# Задание 3. Ближайшая к A точка на плоскости.
from math import sqrt

print("=" * 60)
print("Задание 3. Ближайшая к A точка")
print("\n--- ВВОД ДАННЫХ ---")
# Для каждой точки вводим две координаты: x и y.
ax = float(input("Введите x точки A: "))
ay = float(input("Введите y точки A: "))
bx = float(input("Введите x точки B: "))
by = float(input("Введите y точки B: "))
cx = float(input("Введите x точки C: "))
cy = float(input("Введите y точки C: "))

# Расстояние считаем по теореме Пифагора. sqrt берёт квадратный корень.
ab = sqrt((bx - ax) ** 2 + (by - ay) ** 2)
ac = sqrt((cx - ax) ** 2 + (cy - ay) ** 2)

print("\n--- РЕЗУЛЬТАТ ---")
# Сравниваем расстояния и выводим ближайшую точку.
if ab < ac:
    print(f"Ближе точка B ({bx}; {by})")
    print("Расстояние от A:", ab)
elif ac < ab:
    print(f"Ближе точка C ({cx}; {cy})")
    print("Расстояние от A:", ac)
else:
    print(f"Точки B ({bx}; {by}) и C ({cx}; {cy}) равноудалены от A")
    print("Расстояние от A до каждой точки:", ab)
print("=" * 60)
