my_file = open(r"file.txt")
with open(r"file.txt") as file:
    print(f"Количество строк в файле - {len(file.readlines())}")
my_file = open(r"file.txt")
lines = my_file.readlines()
for i,value in enumerate(lines):
    print(f"Количество символов в {i+1} строке - {len(lines[i])-1}")
my_file = open(r"file.txt")
content = my_file.read()
content = content.split()
print(f"Общее количество слов - {len(content)}")
my_file.close()