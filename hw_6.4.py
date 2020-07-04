class Car:
    ''' Car '''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"New car: {self.name} (color {self.color}) police car - {self.is_police}")

    def go(self):
        print(f'{self.name}: The car goes')

    def stop(self):
        print(f'{self.name}: The car stops')

    def turn(self, direction):
        print(f'{self.name}: The car turns {"left" if direction == 0 else "right"}')

    def speed(self):
        return f'{self.name}: The speed is: {self.speed}'

class CityCar(Car):
    ''' City car '''

    def speed(self):
        return f'{self.name}: The speed is: {self.speed}. Too fast.' if self.speed > 60 else f"{self.name}: The speed is: {self.speed}"

city_car = CityCar("City car", "red", 70)
city_car.go()
print(city_car.speed())
city_car.turn(0)
city_car.stop()
print()


