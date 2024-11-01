from tkinter import *  
import turtle


screen = turtle.Screen()





t = turtle.Pen() 
#turtle.bgcolor('black') 
t.shape("turtle")

#t.pencolor('white')
t.pensize(5)

#star 3
'''
while True:
    t.forward(250)
    t.left(150)
    if abs(t.pos()) < 1:
        break
'''
#heaxagon circle
'''
for x in range(2):
    for repetitions in range(6):
        while True:
                t.forward(100)
                t.left(60)
                if abs(t.pos()) < 1:
                    break
        t.left(60)
    t.left(30)
'''
#square circle
'''
for x in range(3):
    for repetitions in range(6):
        while True:
                t.forward(100)
                t.left(90)
                if abs(t.pos()) < 1:
                    break
        t.left(90)
    t.left(30)
'''
#square pattern
'''
t.pensize(10)
for x in range(2):
    for repetitions in range(6):
        while True:
                t.forward(100)
                t.left(90)
                if abs(t.pos()) < 1:
                    break
        t.left(90)
    t.left(45)
'''
#star 1
'''
while True:
    t.forward(250)
    t.left(170)
    if abs(t.pos()) < 1:
        break
'''
#heart
def curve(): 
    for i in range(200): 
  
        # Defining step by step curve motion 
        t.right(1) 
        t.forward(1) 



def circle():
    for i in range(360): 
  
        # Defining step by step curve motion 
        t.right(1) 
        t.forward(1) 
def circle(steps):
    for i in range(360): 
  
        # Defining step by step curve motion 
        t.right(1) 
        t.forward(steps) 
# Defining method to draw a full heart 
def heart(): 
  
    # Set the fill color to red 
    #t.fillcolor('red') 
  
    # Start filling the color 
    t.begin_fill() 
  
    # Draw the left line 
    t.left(140) 
    t.forward(113) 
  
    # Draw the left curve 
    curve() 
    t.left(120) 
  
    # Draw the right curve 
    curve() 
  
    # Draw the right line 
    t.forward(112) 
  
    # Ending the filling of the color 
    #t.end_fill() 

#flower
'''
for repetitions in range(9):
    heart()
    t.left(180)
'''
#flower outline
'''
for repetitions in range(6):
    curve()
    t.left(140)
'''
#circle pattern
'''
t.pensize(15)
for repetitions in range(8):
    circle()
    t.left(45)

t.left(180)
t.penup()
t.forward(1000)
'''
#reset()
#star 3
'''
while True:
    t.forward(200)
    t.left(140)
    if abs(t.pos()) < 1:
        break
'''
#long pattern circle cone
'''
for i in range(10):
     #t.teleport(20,-75)
     t.circle(5+i*5)
     t.left(90)
     t.forward(10)
     t.right(90)
'''
#triangle
'''
for i in range(15):
     t.forward(10+i*10)
     t.left(120)
'''
#hexagon
'''
for i in range(30):
     t.forward(10+(i/6)*15)
     t.left(60)
'''
#long design chain of circles
'''
t.circle(20)
for i in range(10):
    t.forward(20)
    t.circle(20)
'''
#long design, rectangles
t.teleport(-80,-80)
for i in range(7):
    for j in range(3):
        t.forward(50)
        t.left(80)
        t.forward(50)
        t.left(80)
        t.forward(50)
        t.left(80)
        t.forward(50)
        t.left(80)
        t.forward(30)
        t.left(100)
    '''
    for j in range(2):
        t.right(300)#right 20 = circle design, 280 zigzag
        t.forward(30) 
        t.forward(50)
        t.left(80)
        t.forward(50)
        t.left(80)
        t.forward(50)
        t.left(80)
        t.forward(50)  
    '''
t.penup()
t.forward(200)
t.right(90)
t.forward(1000)
ts = turtle.getscreen()

ts.getcanvas().postscript(file="pattern2.eps")



screen.exitonclick()



num_steps = 5





#for screenshots of code to make stamps of
#turtle.forward(num_steps)

#turtle.left(90)

#turtle.right(90)

#t = turtle.Pen() 

#turtle.teleport()

#turtle.stamp()

#turtle.pendown()

#turtle.penup()

#0

