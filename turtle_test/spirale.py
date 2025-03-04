import turtle

# Deklarationsteil
def spirale(radius):
	alt_x = turtle.xcor()
	alt_y = turtle.ycor()
	speed = 1
	while turtle.distance(alt_x, alt_y) < radius:
		turtle.forward(speed)
		turtle.left(10)
		speed += 0.1

# Hauptprogramm

spirale(75)

turtle.exitonclick()
