import random

with open('number.txt', 'w', encoding='UTF-8') as file:
    glue = ''
    for _ in range(5):
        file.write(glue + str(random.randint(0, 10)))
        glue = ' '

with open('number.txt', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")
