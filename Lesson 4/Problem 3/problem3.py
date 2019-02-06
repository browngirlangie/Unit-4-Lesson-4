from turtle import *

kitkat = Turtle()

kitkat.color("yellow")
kitkat.pensize(12)
kitkat.speed(10)
kitkat.shape("turtle")

for x in range(6):
	kitkat.forward(100)
	kitkat.left(60)

mainloop()