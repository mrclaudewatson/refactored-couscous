# Functions - may be void or value-returning

# ----------function definitions-----------
# void function
def fun1():  # function header
    print('This is in a void function.')
    # return #used to exit the function (unnecessary)


# def fun1(y): #redefinition  - previous version not used (avoid this)
#      print(f'{y} is in a void function.')

# value-returning function
def double(n):  # n is a parameter
    print(f'The original value is {n}.')
    n *= 2
    return n


# ---------main portion------------------
# flow of execution starts here
# functions must be defined before they are called
fun1()  # function call

# test value-returning function
number = int(input('Enter an integer: '))
# number = double(number) #function call in assignment; number is an argument
# print(f'The new value is {number}.')
print(f'The new value is {double(number)}.')  # function call in print statement

# fun1(number) #used to test redefinition

'''
#Run this part separately
#------define a main function------------
def main():
    print('This is now a main function.')

#You still need to call it...
main()
'''

# test if __name__ == "__main__":
#import scratch_9.py