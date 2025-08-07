# Protected attributes (Section 3)
# parent class
class Shape:
    def __init__(self, l, w):
        self._length = l  # single underscore " _ " means attribute is protected. can only be accessed by child classes
        self._width = w   # while double underscores means it is only accessible through THAT clas

    def displaySides(self):
        print(f'Length is {self._length}')
        print(f'Width is {self._width}')


# child class
class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self, l, w)

    def area(self):
        print(f'Area is {self._length * self._width}')
    # main (driver portion)


rect = Rectangle(80, 50)
rect.displaySides()
rect.area()