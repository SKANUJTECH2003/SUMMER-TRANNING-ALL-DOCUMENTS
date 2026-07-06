class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def check_square(self):
        return self.length == self.breadth


if __name__ == "__main__":
    rect1 = Rectangle(8, 5)
    rect2 = Rectangle(6, 6)

    print("Rectangle 1")
    print(f"Area: {rect1.area()}")
    print(f"Perimeter: {rect1.perimeter()}")
    print(f"Is it a square? {rect1.check_square()}")

    print("\nRectangle 2")
    print(f"Area: {rect2.area()}")
    print(f"Perimeter: {rect2.perimeter()}")
    print(f"Is it a square? {rect2.check_square()}")
