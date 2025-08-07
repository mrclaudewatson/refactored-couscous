#UID: U72087839
#Name: Claude Watson
#Drawing Polygons with the turtle module - Draws a polygon from the given number of sides and length, and calculated angle.

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
turtle.color("purple", "black")
for i in range(sides):
    angle = (180 * (sides - 2)) / sides
    angle -= 180
    turtle.forward(length)
    turtle.right(angle)
turtle.done()