# slightly updated code:


# class - blueprint for object
# objects - entity with data and methods (functions that require an object to use it)
'''
class Television:
    #intit method - initializer method - called automatically when an object is created.\
    def __init__(self): # self is the object. Can't call it 'object' because it doesnt exist yet
        self.channel = 1
        self.volume = 1
        #self.__channel = 1 # double underscores hides your data (not required)
        #self.__volume = 1

    # accessor (gettter) methods - get data
    def getchannel(self):
        return self.channel

    def getvolume(self):
        return self.volume

    # mutator (setter) methods - change data
    def setchannel(self, ch):
        self.channel = ch

    def setvolume(self, v):
        self.volume = v

    #othermethods
    def volDown(self):
        if self.volume < 0:
            self.volume -= 1
    def volUp(self):
        if self.volume < 40:
            self.volume += 1

    def chanelDown(self):
        if self.channel > 0:
            self.channel -= 1
    def chanelUp(self):
        if self.channel < 4000:
            self.channel += 1


    # str method - display some info about the object #
    #              automatically called when the object is passed through a print function
    def __str__(self):
        return f"Tv Stats: \nChannel:{self.channel}, Volume:{self.volume}\n"

def main():
    # creates objects
    tv1 = Television()
    tv2 = Television()

    # test str method
    print(tv1)
    print(tv2)

    # test mutators
    tv1.setchannel(58)
    tv1.setvolume(5)

    # test accessors
    print(f"The living room Tv is set to {tv1.getchannel()} and its volume is {tv1.getchannel()}")

    #create local varibales to update tv ibjects
    c = int(input("Enter the channel number:"))
    v = int(input("Enter the tv volume"))

    #update tv ibjects
    tv2.setchannel(c)
    tv2.setvolume(v)

    #confirm update
    print(tv2)



#---call to main---
main()
'''

