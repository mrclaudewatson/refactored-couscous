# UID: U72087839
# Name: Claude Watson
# Description - To calculate the weekly salary f one employee in a specific department

class Employee:
    def __init__(self, n, eid):
        self._name = n
        self._ID = eid


class Engineer(Employee):
    def __init__(self, n, eid, t, hrs):
        Employee.__init__(self, n, eid)
        self.__title = t
        self.__hours = hrs

        self.__payrate = self.getpayrate(self.__title)

    def getpayrate(self, t):
        payrate = {"Engineering Intern": 20, "Senior Engineer": 45, "Lead Engineer": 70}
        return payrate[t]

    def calcpay(self):
        if self.__hours > 40:
            return self.__payrate * 40 + (self.__payrate * 1.5) * (self.__hours - 40)
        else:
            return (self.__payrate * self.__hours)

    def __str__(self):
        return f"Employee ID: {self._ID}\n{self._name}'s pay this week is ${self.calcpay():.2f}"

# ---Driver---

name = input("Enter the employee's name: ")
ID = input("Enter the employee's ID: ")
title = input("Enter the employee's title: ")
hours = int(input("Enter the number of hours worked: "))

while hours < 0 or hours > 60:
    hours = int(input("Enter the number of hours worked: "))

obj = Engineer(name, ID, title, hours)
print(obj)


