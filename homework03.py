def my_func(arg1, arg2, arg3):
    if (arg1 + arg2) > (arg1 + arg3) and (arg1 + arg2) > (arg2 + arg3):
        return arg1 + arg2
    if (arg1 + arg3) > (arg1 + arg2) and (arg1 + arg3) > (arg2 + arg3):
        return arg1 + arg3
    if (arg2 + arg3) > (arg1 + arg2) and (arg2 + arg3) > (arg1 + arg3):
        return arg2 + arg3

arg1 = float(input("Введите значение аргумента 1: "))
arg2 = float(input("Введите значение аргумента 2: "))
arg3 = float(input("Введите значение аргумента 3: "))

print(f"Сумма двух наибольших аргументов: {my_func(arg1, arg2, arg3)}")