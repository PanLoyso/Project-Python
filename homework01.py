def simple_calc():
    x = float(input("Введите количество отработанных часов : "))
    y = float(input("Введите ставку оплаты труда за 1 час : "))
    c = float(input("Укажите сумму премии - "))
    pay = x * y
    return pay + c
print(f"Размер заработной платы сотрудника: {simple_calc() }")