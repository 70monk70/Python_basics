class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Cкорость {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f'Скорость {self.name} превышает разрешенную'
        else:
            return f'Скорость {self.name} не превышает разрешенную'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную'
        else:
            return f'Скорость {self.name} не превышает разрешенную'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
           return f'{self.name} является полицейской машиной'
        else:
            return f'{self.name} не является полицейской машиной'

audi = TownCar(80,'белая', 'Audi', False)
ferrari = SportCar(180, 'красная', 'Ferrari', False)
ford = WorkCar(40, 'черная', 'Ford', False)
oka = PoliceCar(20, 'сине - белая', 'Ока', True)

print(ford.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{ford.go()} со скоростью {ford.show_speed()}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{ford.name} полицейская машина? {ford.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.show_speed())
print(oka.police())
