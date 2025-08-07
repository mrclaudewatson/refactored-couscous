#variable - named space in  memory
#declaring a variable; = means assignment 
var = 56 #assignment is always RHS assigned to LHS (56 = var will not work)
print('The value in var is', var) #echo printing

'''
Idenitifier rules:
1) use letters, digits, underscore _ (in any length)
2) can't statrt with a digit
3) can't use reserved (key) words
4) case sensitive (x, X are different)
'''
#can update a variable with value (or type)
var = 34.78
print(f'The value in var is {var}') #echo printing using an f string

#printing with multiple variables (using f string)
#\ to extend a statement
monday = 245
tuesday = 167
wednesday = 598
print(F"On Monday we sold {monday} kits, on Tuesday we sold \
{tuesday} kits, and on Wednesday we sold {wednesday} kits.")

#printing with multiple variables (without f string)
print('On Monday we sold', monday, 'kits, on Tuesday we sold',
      tuesday, 'kits, and on Wednesday we sold', wednesday, 'kits.')

#input statement (with string prompt)
name = input('Enter your name: ')
print(f'Hello, {name}!')

#input statement (with integer and floating point data)
length = int(input('Enter length: '))
width = float(input('Enter width: '))

#calculate area
area = length * width #mixed expression int * float = float
print(f'The area is {area}')

#for 'constants' use uppercase (and leave it alone)
MAX_SEATS = 90

'''
Symbols for calculations
add: +
subract: -
multiply: *
float division: /
int division: //
remainder (modulus): %
exponent: **
'''
