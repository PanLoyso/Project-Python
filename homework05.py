proceed = int(input("Введите выручку (тыс.руб): "))
outlay = int(input("Введите издержки (тыс.руб): "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = (profitability/proceed) * 100
    print(f"Хорошо. Ваша прибыль {profitability} тыс.руб, рентабельность {rent} %")
    worker = int(input("Сколько у вас сотрудников: "))
    print(f"Ваша прибыль на одного сотрудника составила {profitability/worker} тыс.руб")
elif proceed == outlay:
    print("Не плохо")
else:
    print("Убыток. Требуется пересмотреть ценовую политику")