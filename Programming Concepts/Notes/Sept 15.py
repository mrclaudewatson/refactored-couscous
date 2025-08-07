#fa22wk3lec1
#Week 3 Lecture 1 ('Labor Day' lecture - all sections)

#Compound Assignment - see also section 2.6 in zyBook
number = 10 #given a variable...
print(f'original number is {number}') #echo printing

#... you can update its value by writing the following... 
number = number % 7
print(f'number is now {number}') 

#...or you can can condense the update statement using compound assignment
number %= 7  #This is equivalent to number =  number % (7)

#Note that the 7 is in (). The RHS of the expression will be in () when expanded
#Important to remember this as it can affect operator precedence!
print(f'number is now {number}') 

#Examples of other compound operators below:
number += 9
print(f'number is now {number}')
number -= 1
print(f'number is now {number}')
number /=4 #note: number becomes a float here
print(f'number is now {number}')
number *= 5
print(f'number is now {number}')
number //=3 #note: integer division is still performed on a floating pt number
print(f'number is now {number}')
number **= 2
print(f'number is now {number}')
#------------------------------------------------

#The random module - great for many applications!
#First let's import it. Remember, you can use from to import one or more
#specific functions, but for now we'll import the whole module
import random

#Let's check out some functions:
r = random.random() #generates number between 0 (inclusive) and 1 (exclusive)
print(f"Here's a random number: {r}")
print(f"Here's the same number to 7 decimal place: {r:.7f}") #decimal formatting
print(f"Here's the same number as a percentage: {r:.3%}") #decimal and percent formatting
r2 = random.random() * 5 #expand the range by multiplying
print(f"Here's a random number between 0 and 5(exclusive): {r2}")

#You can shift the the range by adding or subracting. Make sure you figure out the full
#range you want or the results can be unexpected!
r3 = random.random() * 10 - 5   
print(f"Here's a random number in the range [-5, 5): {r3}")

#To avoid using addtional math as in the above, you could use the uniform method instead...
r4 = random.uniform(3, 9) #generates a random float in this range
#upper limit may be included due to rounding
print(f"Here's a random number in the range 3 to 9: {r4}")

#for integers, you can use randint
s = random.randint(1, 6) #generates integer (both limits inclusive)
print(f"Here's a random integer between 1 and 6: {s}")

#...or you can use randrange
s2 = random.randrange(1, 7) #generates integer (upper limit exclusive)
print(f"Here's another random integer between 1 and 6: {s2}")
