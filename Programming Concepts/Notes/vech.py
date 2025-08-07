# Inheritance nov10
# class file
# parent (or super, base) class
class Vehicle:
    # __init__ method
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # accessors
    def getmake(self):
        return self.__make

    def getmodel(self):
        return self.__model

    def getyear(self):
        return self.__year


# child (or sub, derived) class
class Car(Vehicle):  # establish inheritance (parent class in () )
    # __init__ method
    def __init__(self, make, model, year, doors):
        # call the parent class's init method
        Vehicle.__init__(self, make, model, year)
        # set up any addtional attributes (specific to Car objects)
        self.__doors = doors

    def getdoors(self):
        return self.__doors


# child class for child class
class ElectricCar(Car):
    # __init__ method
    def __init__(self, make, model, year, doors, batvolt):
        # call the parent class's init method
        Car.__init__(self, make, model, year, doors)
        # set up any addtional attributes (specific to ElectricCar objects)
        self.__batvolt = batvolt  # batvolt - battery voltage

    def getbatvolt(self):
        return self.__batvolt
