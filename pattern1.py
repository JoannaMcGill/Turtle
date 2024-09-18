from tkinter import *  # Python 3
#from Tkinter import *  # Python 2
import turtle


#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('white') 
t.shape("turtle")
#t.color('green')

#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'grey', 'black', 'pink'] 

for steps in range(9):
    #t.pencolor(colors[steps%9]) 
    t.left(200) 
    #star 2, range 4, left 90
    #star 2, range 9, left 200
    while True:
        t.forward(100)
        t.left(220)
        if abs(t.pos()) < 1:
            break

#save result
ts = turtle.getscreen()

ts.getcanvas().postscript(file="pattern1.eps")

#t.exitonclick()