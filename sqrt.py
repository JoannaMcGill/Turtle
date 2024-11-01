
import turtle
import math

anms = turtle.Turtle()
anms.color("black", "black")
anms.speed(800)
anms.pensize(1)
anms.shape("turtle")
anms.teleport(-100,-100)
anms.begin_fill()

for i in range(300):
    anms.forward(math.sqrt(i))
    anms.left(i%150)
anms.left(150)
for i in range(300):
    anms.forward(math.sqrt(i))
    anms.left(i%150)

anms.end_fill()

turtle.mainloop()
