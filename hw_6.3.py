class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    def full_name(self):
        return f"{self.name} {self.surname}"

    def full_profit(self):
        return f"{sum(self._income.values())}"


ceo = Position("Ivan", "Smith", "CEO", 300000, 100000)
print(ceo.full_name())
print(ceo.position)
print(ceo.full_profit())