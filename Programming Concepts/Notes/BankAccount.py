# class definition:

class Bankinfo:
    def __init__(self, n, ac, bal):
        self.name = n
        self.accnum = ac
        self.balance = bal

    def getname(self):
        return self.name

    def getbalance(self):
        return self.balance

    def getaccnum(self):
        return self.accnum

    def setname(self, n):
        self.name = n

    def setaccnum(self, ac):
        self.accnum = ac

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance >= amt:
           self.balance -= amt
        else:
            print('Insufficient funds.')

    def __str__(self):
        return f'Account Holder: {self.name}, Account Number: {self.accnum}, Account Balance: ${self.balance:.2f}'