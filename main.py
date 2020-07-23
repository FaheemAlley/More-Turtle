import turtle
import math

s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle") # other options include “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
t.color("white") # can put in web color name, or hex value, or RGB value for color
t.speed(0) # 0 is the fastest speed (no animation), 1-10 are animated speeds with 1 being the slowest and 10 being the fastest 
t.pensize(1)

# how to move turtle
t.penup()
t.goto(0,0)
t.pendown()


def square(size):
	for i in range(4):
		t.fd(size)
		t.rt(90)

def triangle(size):
	for i in range(3):
		t.fd(size)
		t.lt(120)

def house(size):
	square(size)
	triangle(size)

def squares(size):
	while size > 0:
		square(size)
		t.penup()
		t.rt(45)
		t.fd(20/math.sqrt(2))
		t.lt(45)
		t.rt(2.5)
		t.pendown()
		size -= 20

def shape(sides, size):
	for i in range(sides):
		t.fd(size)
		t.rt(360.0/sides)

def shapes(sides, size, spacing):
	while size > 0:
		shape(sides, size)
		size -= spacing

def spiro(sides, size, steps, degrees):
	for i in range(360//degrees):
		shape(sides, size)
		t.fd(steps)
		t.rt(degrees)

# spiro(sides = 10, size = 15, steps = 30, degrees = 360//10)

def spiral(nlines, degrees, increase):
	steps = 5
	for i in range(nlines):
		t.fd(steps)
		t.rt(degrees)
		steps += increase

"""sides = 5
spiral(nlines = 1000, degrees = 360/sides + 1, increase = .5)"""

def sphere(size):
	shade = 125
	t.color(0,0,shade)
	while size > 0:
		t.begin_fill()
		shape(30, size)
		t.end_fill()
		t.rt(90)
		t.fd(1)
		t.lt(90)
		size -= .5
		shade += 5
		t.color(0,0,shade)

def pattern():
	sides = 5
	spiral(nlines = 100, degrees = 360/sides + 1, increase = .5)

def moveturtle(x, y):
	t.penup()
	t.goto(x,y)
	t.pendown()

s.onkey(pattern, "F")
s.onclick(moveturtle)
s.listen()
