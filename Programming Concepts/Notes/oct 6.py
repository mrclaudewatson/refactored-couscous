# -----function definitions-----
def main():
    print('Here are some popular games: ')
    esportgames()

    # create a dictionary (slightly expanded from class)
    animals = {'kitty': 'floof', 'dog': 'pupper', 'bird': 'birb', 'snake': 'danger noodle', 'racoon': 'trash panda'}

    # access a specific value, use the dictionary and key
    print(animals['snake'])
    print()

    # call function with a dictionary as a parameter
    newname(animals)
    print()

    # call tekstats, with values out of order
    tekstats('male', 180, 'Jin Kazama', 21)
    print()

    # use keyword arguments to ensure that right value does to right parameter
    tekstats(gender='male', height=180, name='Jin Kazama', age=21)
    print()

    # with default parameters, you can call functions in various ways
    # test default parameters
    printdate(10, 6, 2022, 1)
    printdate(10, 6)
    # printdate(10) #does not work because the second parameter needs a value
    printdate(10, 6, style=2)
    # printdate(day = 6, 10) #does not work; positional arguments need to come first


def esportgames():
    # declaring a list
    games = ['Dota2', 'Fortnite', 'Counter Strike']

    # for loop with enumerate
    for (index, element) in enumerate(games):
        print(f'At number {index + 1}, we have {element}')
    print()

    # to access one value
    print(f'My nephew plays {games[1]}\n')

    # print the list in reverse
    rank = 3
    for i in reversed(games):
        print(f'At number {rank}, we have {i}')
        rank -= 1


def newname(rename):
    # access the contents
    for k in rename:
        print(f'Animal: {k} \t \t Alternate name: {rename[k]}')


def tekstats(name, age, gender, height):
    print(f'Name: {name}\nAge: {age}\nGender: {gender}\nHeight (in cm): {height}')


# use default parameters
def printdate(month, day, year=2022, style=1):
    if style == 1:
        print(f'{month} / {day} / {year}')
    elif style == 2:
        print(f'{day} / {month} / {year}')
    elif style == 3:
        print(f'{year} / {month} / {day}')
    else:
        print('Invalid')

    # -----call to main-----


main()
