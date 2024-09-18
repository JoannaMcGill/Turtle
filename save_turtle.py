from tkinter import *  # Python 3
#from Tkinter import *  # Python 2
import turtle


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x//100 + 1) 
    t.forward(x) 
    t.left(59) 

#save result
ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")