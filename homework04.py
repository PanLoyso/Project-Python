# Первый вариант решения
def my_func(x, y):
    return x ** y
x = float(input("Введите основание степени: "))
y = int(input("Введите показатель степени: "))
print(my_func(x, y))
# Второй вариант решения
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(
    float(input("Введите основание степени: ")),
    int(input("Введите показатель степени: "))
))


