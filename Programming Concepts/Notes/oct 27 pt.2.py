#COP 2510 Section 3 Week 10 Lecture 2 Material
#Wrap up of containers and methods

#Recap of dictionaries and some of their methods
n = int(input('Enter the dictionary size: '))
d1 = dict()

#use a for loop to fill the dictionary
for i in range(1, n+ 1):
    d1[i] = i * 2  #i in d1[i] is the key; value is  i * 2
    #d1[i * 2] = i#this works as well
print(d1)

#can always add literal pairs or variables to add to the dictionary
d1[100] = 200
print(d1)

#you can also use update method to add pairs
d1.update({15: 30} )
key = 20
val = 40
d1.update({key: val})
print(d1)

#to remove pairs use pop(key) by providing a key
d1.pop(2)
print(d1)

#to remove the last pair use popitem()
d1.popitem()
print(d1)

print(d1.keys()) #print keys
#to return the size of the dictionary use len
print(len(d1))
#----------------------------------------------------------------

#Discussed in class: list comprehension - create a new list by modifying elements of an existing list
listex = [2, 4, 6, 8, 10] #existing list

#note that j represents the element
newlist = [j * 10 for j in listex] #list comprehension (j is a range variable)

#Echo print to compare lists:
print(f'First list: {listex}')
print(f'New list: {newlist}')

#You could apply changes to original list, but note the change in syntax
#note that k represents the index not the element
for k in range(len(listex)):
    listex[k] *= 10

print(f'First list: {listex}')
print(f'New list: {newlist}')
#----------------------------------------------------------------

#Discussed in class: Here are different ways to use list comprehension
#for loop with ternary expression
mylist = [1.5, 2.5, 3.5, 4.5, 5.5]
yourlist = [ ]

for m in mylist:
    m = m + 5 if m > 3 else m + 9 #ternary expression
    yourlist.append(m)

print(f'My list: {mylist}')
print(f'Your list: {yourlist}')

#alternative: list comprehension with a ternary expression
ourlist = [m + 5 if m > 3 else m + 9  for m in mylist ] #ternary expression first, then for loop
print(f'Our list: {ourlist}')

#list comprehension with an if statement (note the if clause is moved to the end)
theirlist = [m + 5 for m in mylist if m > 3 ]

print(f'Their list: {theirlist}')
#----------------------------------------------------------------

#sets and set functions
s1 = {1, 2, 3, 4, 5 }
s2 = {2, 4, 5, 6, 7}

#union - combine unique elements of two sets to create a  third set
#commutative s1 union set 2 is same as s2 union s1
s3 = s1.union(s2)
print(f'The union of {s1} and {s2} is {s3}')

#intersection - get comment elements of both sets and store in a third set
#commutative s1 intersection set 2 is same as s2 intersection s1
s4 = s1.intersection(s2)
print(f'The intersection of {s1} and {s2} is {s4}')

#difference - get values from one set that is not in the other set
#NOT commutative
s5 = s1.difference(s2)
s6 = s2.difference(s1)
print(f'The difference of {s1} and {s2} is {s5}')
print(f'The difference of {s2} and {s1} is {s6}')

#symmetric difference - comibines elements that are not common to both set
#think as "union of differences"
s7 =  s1.symmetric_difference(s2)
print(f'The symmetric difference of {s1} and {s2} is {s7}')
