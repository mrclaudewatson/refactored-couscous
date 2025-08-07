# UID: U72087839
# Name: Claude Watson
# Description: To create a class of retail items containing their information. The information will be given by the user
#              and then be printed in a table.

class Retail_Item:
    def __init__(self, t, a, p):
        self.__type = t
        self.__amount = a
        self.__price = p

    def __str__(self):
        return f'{self.__type:<14} {self.__amount:<14} ${self.__price}'


def main():
    name1 = input("Name of item 1: ")
    amount1 = int(input("Amount of item 1: "))
    price1 = float(input("Price of item 1: "))

    name2 = input("\nName of item 2: ")
    amount2 = int(input("Amount of item 2: "))
    price2 = float(input("Price of item 2: "))

    item1 = Retail_Item(name1, amount1, price1)
    item2 = Retail_Item(name2, amount2, price2)

    print("\nHere is a summary of the items you added:\n")
    print(f'{"Item":15}{"Amount":15}{"Price":15}')
    print("-" * 36)

    print(item1)
    print(item2)


main()
