from abc import ABC
from abc import abstractmethod


class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @abstractmethod
    def consumption(self):
        pass

    @property
    def full_consumption(self):
        return (f'Общий расход ткани равен: '
                f'{round(((self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)), 2)}')


class Coat(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)

    def consumption(self):
        return f'Расход ткани на пальто: {round((self.size / 6.5 + 0.5), 2)}'


class Suit(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)

    def consumption(self):
        return f'Расход ткани на костюм: {round((self.growth * 2 + 0.3), 2)}'


coat = Coat(13, 1)
suit = Suit(13, 1)
print(coat.consumption())
print(suit.consumption())
print(coat.full_consumption)
# Возможно ли построить внутри классов такую логику, чтобы инициализировать
# объекты через один аргумент (например, для Coat - 13(size))? # А при подсчете общих затрат ткани,
# вычисление проводилось бы по обоим объектам
