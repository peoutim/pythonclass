#/****************************************************************************
#    Section ?
#    Computer Project #2
#****************************************************************************/

#Program to draw a pentagon

import turtle
import math

print 'This program will draw a congruent pentagon.  The user may choose a red'
print 'green, blue ration to make the internal fill color of the pentagon.'
print 'The user will also input the length of the pentagon sides.'

red = float(raw_input('What is the red value (0-1): ')) #user imput for color
green = float(raw_input('What is the green value (0-1): '))
blue = float(raw_input('What is the blue value (0-1): '))
length = int(raw_input('What is the length of a pentagon side: '))

pred = float(1-red) #values for the pen color from inverse of fill color
pgreen = float(1-green)
pblue = float(1-blue)

x1 = length*-0.5
#calculates x coordinate of bottom left corner of pentagon

y1 = -length/10*math.sqrt(25+10*(math.sqrt(5)))
#calculates y coordinate of bottom left corner of pentagon

turtle.up()
turtle.goto(x1,y1) #move turtle from origin so final pentagon is centered
turtle.pencolor(pred, pgreen, pblue) #pencolor is inverse of fill color
turtle.pensize(5)
turtle.fillcolor(red, green, blue) #colors the inside of the pentagon
turtle.begin_fill()
turtle.down() #turtle only draws when pen is down
turtle.forward(length) #draw one side of pentagon
turtle.left(72) #change pen angle to draw next side of pentagon
turtle.forward(length)
turtle.left(72)
turtle.forward(length)
turtle.left(72)
turtle.forward(length)
turtle.left(72)
turtle.forward(length)
turtle.end_fill()
turtle.up() #turtle will not draw with pen up
turtle.right(18)
turtle.forward(20)
turtle.write('R:'+(str(red))+'  ', move=True, align='left', font=('Arial', 8, 'normal'))
turtle.write('G:'+(str(green))+'  ', move=True, align='left', font=('Arial', 8, 'normal'))
turtle.write('B:'+(str(blue))+'  ', move=False, align='left', font=('Arial', 8, 'normal'))
turtle.hideturtle()

import time #keep turtle window open
time.sleep(30)

import os
os._exit(1)
