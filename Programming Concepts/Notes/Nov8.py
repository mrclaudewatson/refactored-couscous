# class file - app

class App:
    # __init__ method
    def __init__(self, name, typ):
        self.__appname = name
        self.__apptype = typ

    # str method
    def __str__(self):
        return self.__appname.ljust(25) + self.__apptype.ljust(25) # ljust adjusts it left and the 25 is the field width

