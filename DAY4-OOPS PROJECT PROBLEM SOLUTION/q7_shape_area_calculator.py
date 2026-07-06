import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6), Triangle(8, 3)]
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")
