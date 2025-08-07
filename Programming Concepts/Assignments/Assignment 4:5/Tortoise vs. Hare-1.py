#UID: U72087839
#Name: Claude Watson
#Tortoise vs. Hare - To simulate a race between a tortoise and a hare up a slippery hill.


import turtle
import random


def toddmove(currentpos):  # function to determine Todd's movement
    num = random.randint(1, 10)

    if todd.xcor() < -100:  # resets the racer's position if it passes -100 or 100.
        todd.setpos(-100, 0)
    elif todd.xcor() > 100:
        todd.setpos(100, 0)

    if num >= 1 and num <= 5:  # probability
        currentpos += 3
    elif num >= 6 and num <= 7:
        currentpos += -5
    elif num >= 8 and num <= 10:
        currentpos += 1

    return currentpos


def harrymove(currentpos):  # function to determine Harry's movement
    num = random.randint(1, 10)

    if harry.xcor() < -100:  # resets the racer's position if it passes -100 or 100.
        harry.setpos(-100, 50)
    elif harry.xcor() > 100:
        harry.setpos(100, 50)

    if num >= 1 and num <= 2:  # probability
        currentpos += 0
    elif num >= 3 and num <= 4:
        currentpos += 7
    elif num == 5:
        currentpos += -10
    elif num >= 6 and num <= 8:
        currentpos += 1
    elif num >= 9 and num <= 10:
        currentpos += -2

    return currentpos


start = turtle.Turtle()  # sets up the starting line
start.hideturtle()
start.speed(99999999)
start.color("black")
start.penup()
start.setpos(-100, 100)
start.write("Start", move=False, align='center', font=('Arial', 18, 'normal'))
start.pendown()
start.right(90)
start.forward(150)

finish = turtle.Turtle()  # sets up the finish line
finish.hideturtle()
finish.speed(99999999)
finish.color("black")
finish.penup()
finish.setpos(100, 100)
finish.write("Finish", move=False, align='center', font=('Arial', 18, 'normal'))
finish.pendown()
finish.right(90)
finish.forward(150)

todd = turtle.Turtle()  # set up Todd
todd.speed(1)
todd.penup()
todd.color("green")
todd.shape("turtle")
todd.setpos(-100, 0)

harry = turtle.Turtle()  # sets up Harry
harry.speed(1)
harry.penup()
harry.color("brown")
harry.shape("square")
harry.setpos(-100, 50)

clock = 0
while todd.xcor() < 100 and harry.xcor() < 100:  # loop to make Harry and Todd move forward
    clock += 1  # adds 1 to the clock during each iteration.

    todd.forward(toddmove(0))
    harry.forward(harrymove(0))

    if todd.xcor() >= 100 and harry.xcor() >= 100:  # condition if tie
        todd.setpos(100, 0)
        winner = turtle.Turtle()
        winner.hideturtle()
        winner.speed(99999999999)
        winner.color("green")
        winner.penup()
        winner.setpos(135, 200)
        winner.write(f"Todd the tiny tortoise has won! \nTime of race: {clock} seconds", move=False, align='center',
                     font=('Arial', 18, 'normal'))

    if todd.xcor() >= 100:  # condition if Todd wins
        todd.setpos(100, 0)
        winner = turtle.Turtle()
        winner.hideturtle()
        winner.speed(99999999999)
        winner.color("green")
        winner.penup()
        winner.setpos(135, 200)
        winner.write(f"Todd the tiny tortoise has won! \nTime of race: {clock} seconds", move=False, align='center',
                     font=('Arial', 18, 'normal'))

    elif harry.xcor() >= 100:  # condition if Harry wins
        harry.setpos(100, 50)
        winner = turtle.Turtle()
        winner.hideturtle()
        winner.speed(99999999999)
        winner.color("brown")
        winner.penup()
        winner.setpos(135, 200)
        winner.write(f"Harry the hairy hare has won! \nTime of race: {clock} seconds", move=False, align='center',
                     font=('Arial', 18, 'normal'))

    if todd.xcor() < -100: # extra condition to reset x cor if it goes below x = -100
        todd.setpos(-100, 0)
    elif harry.xcor() < -100:
        harry.setpos(-100, 50)

    if todd.xcor() > 100:  # extra condition to ensure final position is x = 100
        todd.setpos(100, 0)
    elif harry.xcor() > 100:
        harry.setpos(100, 50)

turtle.done()