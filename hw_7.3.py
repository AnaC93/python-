class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.numbers // rows)]) + '\n' + '*' * (self.numbers % rows)

    def __str__(self):
        return self.numbers

    def __add__(self, other):
        return f'The sum of cells is: {self.numbers + other.numbers}'

    def __sub__(self, other):
        return self.numbers - other.numbers if self.numbers - other.numbers > 0 \
            else "Impossible to subtract"

    def __mul__(self, other):
        return f'The product of multiplication is: {self.numbers * other.numbers}'

    def __divmod__(self, other):
        return f'The result of division is: {round(self.numbers / other.numbers)}'


