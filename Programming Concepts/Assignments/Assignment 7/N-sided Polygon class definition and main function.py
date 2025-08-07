# UID: U72087839
# Name: Claude Watson
# Description: Create a class to calculate and the display the area and perimeter of a polygon, given the number of
#              sides and the length for each side.


import math


class Polygon:
    def __init__(self):  # initializer
        self.__sides = 0
        self.__length = 0.0

    def getperimeter(self):  # perimeter accessor
        return self.__sides * self.__length

    def getarea(self):  # area accessor
        return (self.__sides * self.__length**2) / (4 * math.tan((math.pi/self.__sides)))

    def setside(self, s):  # sides mutator
        self.__sides = s

    def setlength(self, l):  # length mutator
        self.__length = l


def main():
    shape = Polygon()  # object creation

    sides = int(input("Enter the number of sides for your polygon (>= 3): "))
    while sides < 3:
        sides = int(input("Enter the number of sides for your polygon (>= 3): "))
    shape.setside(sides)  # sets self.__sides to local variable sides

    length = float(input("How long would you like each side to be? (>= 0.1: "))
    while length < 0.1:
        length = float(input("How long would you like each side to be? (>= 0.1:): "))
    shape.setlength(length)  # sets self.__length to local variable length

    print(f"The polygon has {sides} sides, with a length of {length} for each side.")
    print(f"The area for your polygon is {shape.getarea():.3f} square units, while the perimeter is "
          f"{shape.getperimeter():.3f} units.")


main()
