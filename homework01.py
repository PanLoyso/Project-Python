a = int(5)
b = float(2.4)
c = str("Привет")
d = [20, 30, 40]
e = {"haracter": "elf", "profession": "archer"}
f = ("John", 10)
list = [a, b, c, d, e, f]
for i in list:
    print(f"{i} is {type(i)}")
