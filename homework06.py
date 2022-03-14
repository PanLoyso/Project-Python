#итератор, генерирующий целые числа, начиная с указанного
from itertools import count, cycle

print("Итератор, генерирующий целые числа, начиная с указанного:")
for item in count(3):
    if item > 10:
        break
    else:
        print(item)

#итератор, повторяющий элементы некоторого списка, определенного заранее
print("\nИтератор, повторяющий элементы некоторого списка, определенного заранее:")
count = 0
for item in cycle([1, 2, 3]):
    if count > 8:
        break
    print(item)
    count += 1