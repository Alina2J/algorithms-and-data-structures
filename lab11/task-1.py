# Лабораторная 11. Обход бинарного дерева поиска.
class Node:
    def __init__(self, value):
        # Узел хранит число и ссылки на двух потомков.
        # None означает, что соответствующего поддерева пока нет.
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    # Пустое место становится новым узлом дерева.
    if root is None:
        return Node(value)
    # Меньшие значения направляем влево, остальные, включая равные, — вправо.
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    # Возвращаем корень, чтобы сохранить связь с построенным поддеревом.
    return root


def inorder_traversal(root, result):
    # Дошли до отсутствующего потомка — возвращаемся к предыдущему вызову.
    if root is None:
        return
    # Сначала обходим всё левое поддерево, затем посещаем текущий узел,
    # после чего обходим правое поддерево. Каждый узел посещается один раз.
    inorder_traversal(root.left, result)
    result.append(root.value)
    inorder_traversal(root.right, result)


def print_tree(root, prefix="", label="Корень: "):
    if root is None:
        return
    # Отступ показывает уровень вложенности, подпись — сторону относительно родителя.
    print(prefix + label + str(root.value))
    print_tree(root.left, prefix + "    ", "Левый: ")
    print_tree(root.right, prefix + "    ", "Правый: ")


print("=" * 60)
print("Лабораторная 11. Обход бинарного дерева поиска")
print("\n--- ВВОД ДАННЫХ ---")
print("Введите числа в порядке добавления в дерево. Первое число станет корнем.")
print("Пример: 50 30 20 40 70 60 80")

while True:
    try:
        n = int(input("Количество узлов N (> 0), одно число: "))
    except ValueError:
        print("Введите одно целое число, например 7.")
        continue
    if n <= 0:
        print("Количество узлов должно быть положительным.")
        continue
    break

while True:
    try:
        # Разбиваем ввод по пробелам и превращаем каждую часть в целое число.
        numbers = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()))
    except ValueError:
        print("Введите только целые числа через пробел. Повторения допускаются.")
        continue
    if len(numbers) != n:
        print(f"Нужно ровно {n} чисел. Сейчас введено: {len(numbers)}.")
        continue
    break

# Начинаем с пустого дерева. Каждый вызов insert добавляет один узел.
tree = None
for value in numbers:
    tree = insert(tree, value)

print("\n--- ПОСТРОЕННОЕ ДЕРЕВО ---")
print_tree(tree)

# Передаём пустой список: при обходе в него добавятся значения посещённых узлов.
traversal = []
inorder_traversal(tree, traversal)

print("\n--- РЕЗУЛЬТАТ ---")
print("Обход: левое поддерево -> корень -> правое поддерево.")
print("Порядок посещения узлов:", " -> ".join(map(str, traversal)))
print("В бинарном дереве поиска этот обход даёт значения по возрастанию.")
print("=" * 60)
