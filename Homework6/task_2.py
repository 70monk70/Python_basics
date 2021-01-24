class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, mass, depth):
        self.mass = mass
        self.depth = depth
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: '
              f'{(Road._length * Road._width * mass * depth) / 1000} т')


Road = Road(20, 5000)
Road.calculation(25, 5)
