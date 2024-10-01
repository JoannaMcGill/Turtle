from tkinter import *  
import turtle


screen = turtle.Screen()

#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('white') 
t.shape("turtle")
#t.color('green')

#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'grey', 'black', 'pink'] 
t.pencolor('black')
t.stamp()
'''
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
t.shape('circle')
t.color('black')
t.stamp()
#t.penup()
#t.forward(10000)
#save result
#t.teleport(10000,10000)
'''
t.penup()
for steps in range(100):
    t.left(180)
    t.stamp()
    t.left(180)
    t.forward(steps)
    t.right(50)
    t.left(100)

ts = turtle.getscreen()

ts.getcanvas().postscript(file="pattern2.eps")
#time.sleep(5)


screen.exitonclick()