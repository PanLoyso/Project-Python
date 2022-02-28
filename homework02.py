a = int(input("Введите значение >>> "))
b = int(input("Введите значение >>> "))
c = int(input("Введите значение >>> "))
d = int(input("Введите значение >>> "))
numbers = [a, b, c, d]
numbers[::2], numbers[1::2] = numbers[1::2], numbers[::2]
print(numbers)