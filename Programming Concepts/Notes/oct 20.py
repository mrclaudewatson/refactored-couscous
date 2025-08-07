# function that accepts two values and returns a list
def multiples(v, a):
    mlist = []  # create empty list
    for i in range(1, a + 1):  # last value is omitted so add 1 to include it
        mlist.append(i * v)  # append - adds a value to the list
    return mlist


# function that returns a dictionary
def meaning():
    translate = {'ngl': 'not gonna lie', 'yeet': 'throw'}
    return translate


# recursive function example
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# New! Creating lamba functions!
# lambda functions are small anonymous functions. They can take many parameters,
# but only one expression.
# They can be embedded in an assignment statement...
val = lambda x: x + 4  # x is the parameter, x + 4 is the expression


def main():
    value = float(input('What is the starting value? '))
    amt = int(input('How many multiples would you like to see? '))

    # call multiples function in print statement
    print(f'The first {amt} multiples of {value} are:\n{multiples(value, amt)}')
    # calling meanings function
    print(f'Here are some terms and their meanings:\n {meaning()}')
    # recursive call (now with user input)
    number = int(input('Enter a number > 1: '))
    print(f'{number}! = {factorial(number)}')
    # calling lambda functions (using previous input)
    print(f'{number} + 4 = {val(number)}')  # .. and called using the variable name
    # you can use lambda fucntions with the conditional (ternary) operator.
    # Note that the definition is in main here:
    minval = lambda a, b: a if a <= b else b
    # call to minval lambda function (now with input)
    n1, n2 = input('Enter two numbers: ').split()
    n1, n2 = float(n1), float(n2)  # note: multiple conversion and assignment!
    print(f'The smaller of {n1} and {n2} is {minval(n1, n2)}')


# -----no function defintions below this line-----
main()  # call to main