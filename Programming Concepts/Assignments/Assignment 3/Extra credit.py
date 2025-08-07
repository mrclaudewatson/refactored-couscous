#UID: U72087839
#Name: Claude Watson
#Extra cedit - To display the name of the polygon based off the number of sides given.

sides = int(input("Enter the number of sides for your shape (between 3 and 12):"))
while sides < 3 or sides > 12:
    print("Invalid entry.", end=" ")
    sides = int(input("Enter the number of sides for your shape (between 3 and 12):"))

length = int(input("Enter the length for each side (greater than 50):"))
while length <= 50:
    print("Invalid entry.", end=" ")
    length = int(input("Enter the length for each side (greater than 50):"))

import turtle
turtle.speed(3)
turtle.color("purple")
for i in range(sides):
    angle = (180 * (sides - 2)) / sides
    angle -= 180
    turtle.forward(length)
    turtle.right(angle)

if sides == 3:
    turtle.color("black")
    turtle.write("Triangle", font = 50, align = "right")
elif sides == 4:
    turtle.color("black")
    turtle.write("Quadrilateral", font = 50, align = "right")
elif sides == 5:
    turtle.color("black")
    turtle.write("Pentagon", font = 50, align = "right")
elif sides == 6:
    turtle.color("black")
    turtle.write("Hexagon", font = 50, align = "right")
elif sides == 7:
    turtle.color("black")
    turtle.write("Heptagon", font = 50, align = "right")
elif sides == 8:
    turtle.color("black")
    turtle.write("Octagon", font = 50, align = "right")
elif sides == 9:
    turtle.color("black")
    turtle.write("Nonagon", font = 50, align = "right")
elif sides == 10:
    turtle.color("black")
    turtle.write("Decagon", font = 50, align = "right")
elif sides == 11:
    turtle.color("black")
    turtle.write("Hendecagon", font = 50, align = "right")
elif sides == 12:
    turtle.color("black")
    turtle.write("Dodecagon", font = 50, align = "right")

turtle.done()