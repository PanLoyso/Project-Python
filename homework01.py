def calculate(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ("Деление на ноль запрещено")
print(calculate(
    int(input("Введите число а >>> ")),
    int(input("Введите число b >>> "))
))