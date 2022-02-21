a = float(input("Ввведите результат тренировки первый день (км): "))
b = float(input("Введите результат тренировок (км): "))
day = 1
while b - a > 0:
    a = a + a/10
    day += 1
print(day)


