#loop else
for i in range(1, 5):
    print(i)
else: #execute if loop runs successfully
    print('Loop ran without interruptions')

#loop else with break
for i in range(1, 5):
    print(i)
    break
else: #does not execuite because of the break
    print('Loop ran without interruptions')

#loop else with continue
for i in range(1, 11):
    if i == 4:
        continue
    print(i)
else: #execute if loop runs successfully
    print('Loop ran without interruptions')
#--------------------------

#nested loops
#for every 1 iteration of the outer loop, the inner loop completes all iterations
    
digit1 = 0
while digit1 <= 9: #outer loop
    digit2 = 0
    while digit2 <= 9: #inner loop
        print(f'{digit1} -- {digit2}')
        digit2 += 1
    digit1 += 1
#--------------------------     

#turtle module
import turtle
turtle.speed(8) #adjust speed (range is 1 to 10 for animation)
turtle.shape("turtle") #change the shape

#to name turtle, use turtle.Turtle() e.g bob = turtle.Turtle()
#use turtle.done() to keep window running

#draw square
for x in range(4):
    turtle.forward(150) #150 is number of pixels
    turtle.right(90)

turtle.clearscreen()

#draw octagon
turtle.shape("turtle") 
for x in range(8):
    turtle.backward(75) #75 is number of pixels
    turtle.dot(10, 'green')
    turtle.right(45)

#draw multiple circles
turtle.clearscreen()
turtle.shape("turtle")
x, y = -250, 0 #use for coord
turtle.penup()
turtle.setpos(x, y)

for z in range(7):
    turtle.pendown()
    turtle.circle(40)
    x += 80
    turtle.penup()
    turtle.setpos(x, y)

turtle.clearscreen()
#create graphics and use 'constants'
NUM_CIRCLES = 36
RADIUS = 80
ANGLE = 10
SPEED = 20
SHAPE = "turtle"

turtle.speed(SPEED)
turtle.shape(SHAPE)

for c in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
    
