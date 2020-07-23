class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = 2 * radius

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = int(self.diameter / 2)

    def __str__(self):
        return "반지름 : {}, 지름 : {}".format(self.radius, self.diameter)

circle1 = Circle(3)

print(circle1)

circle1.diameter = 10

print(circle1)

circle1.radius = 8

print(circle1)