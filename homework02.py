list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [number for i, number in enumerate(list) if i > 0 and list[i] > list[i - 1]]
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)
