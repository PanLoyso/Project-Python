class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


Worker = Position('Петр', 'Иванов', 'Консультант', 90000, 20000)
print(Worker.get_full_name())
print(Worker.position)
print(Worker.get_total_income())