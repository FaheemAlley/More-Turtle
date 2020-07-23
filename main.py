import turtle

turtle.speed(10)

#def spiral(nlines, degrees, increase):
#	steps = 5
#for i in range(nlines):
	#	turtle.fd(steps)
	#	turtle.rt(degrees)
	#	steps += increase
	
#spiral(100, 145, 7)

bowl = turtle.Turtle()


bowl.speed(30)

for larry in range(0,22):
	for counter in range(0,4):
		bowl.forward(100)
		bowl.left(90)
	bowl.left(15)

	bowl.forward(25)
	bowl.left(90)
	bowl.forward(50)
	bowl.right(90)
	bowl.forward(50)
	bowl.right(90)
	bowl.forward(50)
	bowl.right(90)
	bowl.forward(75)



