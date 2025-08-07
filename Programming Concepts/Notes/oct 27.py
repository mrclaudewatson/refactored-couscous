#Intro to file input

popdogs = open('popularbreedsUS.txt', 'r') #open is the function to open a file and 'r' is the function to read the file

#to read the file use readlines()
breeds = popdogs.readlines() #breeds will be a list
popdogs.close()

#print(breeds) #produces squeezed text
'''
#alternate - use the with keyword (don't have to use close() )
with open('popularbreedsUS.txt', 'r') as popdogs:
    breeds = popdogs.readlines()

print(breeds) #produces squeezed text
'''
#remove trailing characters such as \n with rstrip()
doglist = []
for i in breeds:
    d = i.rstrip() #.rstrip() used to removes white spaces
    doglist.append(d)

#print(doglist)

#now you can print some or all of the list
rank = int(input('Enter a rank number: '))
print(f'Here are the top {rank} dog breeds in the US: ')

for index, element in enumerate(doglist):
    print(f'{index + 1}. {element}')
    if index + 1 == rank:
        break
'''
# note:
# readline() - read one line at a time
#popdogs = open("popularbreedsUS.txt", "r")
#doggo = popdogs.readline() # used to read only 1 line (the first line)


#------
#to write to a file
#with open('blah.txt', 'w') as out1:
# out1.write('The weather is great today.')








