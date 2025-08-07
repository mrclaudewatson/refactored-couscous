# driver program (section 3)
#import BankAccount
from BankAccount import Bankinfo
def main():
    #acc1 = BankAccount.Bankinfo("Cloudy", 9102003, 0)  # need to reference file name and class name.
    acc1 = Bankinfo("cloudy",0, 0)
    print(f'At Kiosk 1, an account for {acc1.getname()} has been created')
    print(acc1)

    dep = float(input("How much would you like to deposit?: \n"))

    acc1.deposit(dep)
    print(acc1)



# ---call to main---
main()
