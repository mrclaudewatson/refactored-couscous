#more about strings (container) aka a list of characters
name = 'Schinnel Small'
#len - (length) returns the no. of characters (objects) in the container
print(len(name))
#character check
if 'a' not in name:
    print(f"I didn't find an 'a' in {name}")
else:
    print(f"I did find an 'a' in {name}")
#Recap: for containers, you'll have an index and an element
#index - position; element - value in position
#first index is position 0
#refer to specific index using list notation [ ]
print(name[0])
#but can use -ve indices to get the right most element
#starting from left most position: first position is 0
#starting from right most position: last position is -1
print(name[-3])
#string slicing using [] - obtain substrings
slname = name[0: 5] #obtain chars from 0 inc. to 5 excl. (i.e 4)
print(slname)
#strings are immutable (can't be changed)
#other immutable types: int, float, bool, tuple
#name[1] = 'C' #doesn't work
name = "John Smith" #this works because you are allocating new memory space
print(name)
#list of strings
strlist = ['Oh', 'hello', 'there', 'welcome', 'to', 'COP 2510']
print(strlist) #print out the list
#to access a value, indicate the list and its index
print(strlist[1])
#you can add another dimension to a list of strings by using another set of []
print(strlist[3][1]) #3 - welcome, 1 - e
#mutable - values can be added or changed
strlist [0] = 86.7
print(strlist)
hero = "Finn the Human"
#you can search for sequences as well as characters in the string
if 'her' in hero:
    print("True")
else:
    print("False")
#to add (concatenate) strings together you can 1) use +
sub1 = 'Jake'
sub2 = ' the dog'
sub3 = sub1 + sub2
print(f'sub3 is {sub3}') #or you can use print(f'{sub1 + sub2}')
#or you can 2) use the join method
strlist = ['oh', 'my', 'frog', 'wow']
silly = ' '.join(strlist) #note the use of the string literal
print(f'The phrase in silly is {silly}.')
silly2 = '+'.join(strlist) #note the use of the string literal
print(f'The phrase in silly2 is {silly2}.')
silly3 = sub1.join(strlist) #note the use of the string object
print(f'The phrase in silly3 is {silly3}.')
#more about lists
list1 = [] #empty list
names = ['Jake', 'Jack', 'Jane', 'John', 11, 5] #list can contain different types
print(f'Contents of names: {names}.')
#lists are mutable
names[4] = 'Jason'
print(f'Contents of names: {names}.')
#to populate list1, use append method
n = int(input('How many values to enter (> 0)?'))
for j in range(n):
    s = float(input(f'Enter value {j + 1}: '))
    list1.append(s) #add a value to the end of the list
print(f'Contents of list1: {list1}.')
#to add new values anywhere in a list, use insert
names.insert(1, 'Bob') #give index, then element
names.insert(3, 'Kyle')
names.insert(5, 'Kyle')
print(f'Contents of names: {names}.')
#to remove values from the list, use pop
names.pop() #remove the last element by default
print(f'Contents of names: {names}.')
names.pop(1) #you can specify an index
print(f'Contents of names: {names}.')
#you can also use remove
names.remove('Kyle') #removes the first occurence
#names.remove(names[2]) also works
print(f'Contents of names: {names}.')
#you can append full lists as well lists (to create a nested list)
names.append(list1)
print(f'Contents of names: {names}.')
#to access a value in a nested list, use extra [ ]
#(reminder: will not work if the second list is empty or too short)
#print(names[6][1])
#tuple - sequence a of values, but immutable
#define a tuple by using ()
coord = (4.5, 8.5, 10.6)
print(f'Contents of coord: {coord}.')
#can't do this
#coord [0] = 5.5
#can refer to any position in a tuple by using []
print(f'the x coordinate is: {coord[0]}.')
#enumerate - used to get index as well as element in a list
for (i, j) in enumerate(strlist):
    print(f'{i + 1}. {j}')  # i + 1 prints starting from 1