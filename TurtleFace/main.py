from turtle import *

# how to draw a centered circle
def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    for i in range(60):
        forward(3.14*radius/30)
        left(6)
    right(90)
    back(radius)
    
# how to draw an eye
def eye():
    color('black', 'black')
    circle(50)
    penup()
    forward(25)
    # pupil
    begin_fill()
    circle(25)
    end_fill()
    back(25)

#how to draw a mouth
def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)
        
def centered_arc(radius, angle):
    left(angle/2)
    penup()
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)


# drawing the head
color('orange')
circle(300)

# drawing the left eye
left(90)
forward(150)
left(90)
forward(100)
right(270)     # adjust
eye()

# drawing the right eye
left(90)
forward(200)
right(90)      # adjust
eye()

#drawing the mouth
forward(200)
right(90)
forward(100)
left(90)
color('red')
width(15)
centered_arc(150,90)



hideturtle()
bye()