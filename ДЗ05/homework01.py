my_file = open("test.txt", "w")
if my_file.writable():
    strings = input("Введите текст \n")
    my_file.writelines(strings)
else:
    print("Can not write")

my_file.close()

my_file = open(r"test.txt")
content = my_file.readlines()
print(content)
my_file.close()