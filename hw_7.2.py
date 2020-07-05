from abc import ABC, abstractclassmethod


class Clothes(ABC):

    def __init__(self,param):
        self.param = param

    @abstractclassmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric per coat - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric per costume - {2 * self.param + 0.3}")
        return 2 * self.param + 0.3


coat = Coat(42)
costume = Costume(180)
print(coat + costume)