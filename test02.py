import turtle
def zeichne_quad():
  for i in range(1,5):
      turtle.forward(75)
      turtle.left(90)
 

farben = ["green", "red", "black", "brown" , "blue" , "yellow"]

turtle.shape("turtle")
for i in range(0,24):
  turtle.pencolor(farben[i % 5])
  zeichne_quad()
  turtle.left(15)

turtle.exitonclick()
