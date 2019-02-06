from turtle import *

kitkat = Turtle()

kitkat.color("green")
kitkat.pensize(12)
kitkat.speed(10)
kitkat.shape("turtle")
 
screen = Screen()
screen.bgcolor("yellow")

kitkat.forward(80)
kitkat.right(50)
kitkat.forward(200)
kitkat.left(150)
kitkat.forward(50)
kitkat.circle(25)
kitkat.backwards(300)

mainloop()