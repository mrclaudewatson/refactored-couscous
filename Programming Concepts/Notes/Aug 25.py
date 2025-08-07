#This is a single line comment

'''
print('Welcome to COP 2510!') #output statement
print() #create a blank space

#\n - newline escape sequence - move cursor to a new line
print("It's a great day to learn Python!\n") #output statement with single quote

print('I said "Hello" to you.\n')#output statement with double quote
'''

#python allows triple quotes - 3 single quotes
print('''There was an old man with a beard,
who said "It's just as I feared!
Two Owls and a Hen,
Four Larks and a Wren,
have all built their nests in my beard!"''')

'''You can use this as a "multi-line" comment,
but techncially it is not a comment, just a string.'''

#use \ to print \
print('\\n - newline escape sequence')

#to supress the newline, use the end option
print('3, ', end = ' ')
print('2, ', end = ' ')
print('1.\n')

#another example
print('3, ', end = '...')
print('2, ', end = '...')
print('1.\n')

#use sep to separate strings
print('sksmall', 'usf.edu', sep='@')

#will this work?
#print(“This is a test.”)
