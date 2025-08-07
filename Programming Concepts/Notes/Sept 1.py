#Operator Precedence (check section 2.5 in zyBook)
'''
4 + 6 * 3 / 15 * 6 = 4 + 18 / 15 * 6 = 4 + 1.2 * 6 = 4 + 7.2 = 11.2
4 + (6 * 3) / 15 * 6 = 4 + (18 / 15) * 6 = 4 + (1.2 * 6) = 4 + 7.2 = 11.2
'''
#check section 2.9 in zyBook for math module
import math #access all functions in math module
from math import sqrt, fabs #access to one (or more) specific functions

num =float(input('Enter a positive number: '))
print(f'The square root of {num} is {math.sqrt(num)}') #embed expression in f string

#Alternative, you can save result in a variable
sq = sqrt(num)
print(f'The square root of {num} is {sq}')
print(f'The absolute value of {num} is {fabs(num)}')
#-----------------

#formatting options
#option1: use format function
print('The square root of', num, 'is', format(sq, '.5f')) #.5f - 5 decimal places

#option 2: formatting with % (section 2.11 in zyBook)
age = 7
print('My dog is %d years old (in human years).' % age)

#option 3: formatting with string format function
number = 5
price = 2500000
print('{} items cost ${:,.2f}'.format(number, price))

#option 4: formatting with f string
print(f'{number} items cost ${price:,.2f}') #you can use the , by itself
#-----------------

#multiple input
#option 1: see zyBook challenge 1.3.5
#you can use one prompt and multiple input statements
print('Enter 3 values (press enter after each): ')
x = float(input())
y = float(input())
z = float(input())
print(f'The values entered were {x}, {y} and {z}.')

#option 2: use the split function (with strings) and multiple assisgnment
a, b, c =input('Enter 3 values (separated by spaces: ').split()
print(f'The values entered were {a}, {b} and {c}.')

#for calculations, don't forget to convert
a = float(a)
b = float(b)
c = float(c)

print(f'The sum is {a + b + c}')















