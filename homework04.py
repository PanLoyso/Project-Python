number = int(input("Введите целое положительное число: "))
max = number % 10
print(max)
while number >= 1:
    number = number // 10
    print(number)
    if number % 10 > max:
        print(number)
        print(max)
        max = number % 10
        print(max)
    elif number > 9:
        pass
print("Максимальное цифра в числе: ", max)
