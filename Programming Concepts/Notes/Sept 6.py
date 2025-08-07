#more on for loops
for j in range(1000, 99, -50): #decrement by 50
    print(f'{j}', end = ' ')
print('\n')

#for loop in strings
plan = 'Take a nap after class.'
for p in plan:
    print(f'{p}', end = '...')
print('\n')
    
#for loop in lists
#list - collection of items (may be of different types)
names = ['Carmilla', 'Morana', 'Striga', 'Lenore', 5, 11]

for n in names:
    print(f'Hi {n}!')
print('\n')

#break and continue statements
for v in range(20):
    if v == 13:
        break #interrupts the loop
    print(f'{v}', end = ' ')
print('\n')

#break statement can interrupt nested loop
i = 1
j = 1
while i < 10:
    while j < 10:
        if j == 2:
            break
        print(f'{j}', end = ' ')
        j += 1
    print(f'{i}', end = ' ')
    i += 1
print('\n')

#break statement can interrupt infinite loop
while True:
    print('Spam!', end = ' ')
    break
print('\n')

'''
#don't do this
k = 1
while True:
    if k > 10:
        break
    print(f'{k}', end = ' ')
    k += 1
'''

for w in range(1, 26):
    if w == 4 or w == 13:
        continue #skip current iteration
    print(f'{w}', end = ' ')



























   







