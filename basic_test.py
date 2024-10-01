from turtle import *
import time

def reset():
    home()
    clearscreen()

def move_away():
    penup()
    forward(10000)
    time.sleep(10)
    home()

#triangle
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#reset
#move_away()
reset()

shape("turtle")
'''
#geometric pattern: spiral
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
move_away()
reset()
'''
'''
#altered spiral code
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(50)
        left(100)
move_away()
reset()
'''
'''
#star
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
move_away()
reset()
'''
'''
#star but wider center: star 2
while True:
    forward(200)
    left(220)
    if abs(pos()) < 1:
        break
move_away()
reset()
'''
'''
#star in circle
for steps in range(9):
    left(200) 
    #star 2, range 4, left 90
    #star 2, range 9, left 200
    while True:
        forward(100)
        left(220)
        if abs(pos()) < 1:
            break
move_away()
reset()
'''

#triangle spiral 1
while True:
        forward(100)
        left(220)
        forward(20)
        right(70)
        forward(100)
        left(80)
        if abs(pos()) < 1:
            break

move_away()
reset()

'''
#triangle spiral 2
while True:
        forward(100)
        left(220)
        forward(20)
        right(70)
        forward(100)
        left(80)
        forward(20)
        right(70)
        forward(100)
        left(30)
        if abs(pos()) < 1:
            break
move_away()
reset()
'''
'''
#hexagonal spiral 1
for x in range(250):  
    forward(x) 
    left(59) 
move_away()
reset()
'''
'''
#mini sun
while True:
        forward(10)
        left(220)
        forward(2)
        right(70)
        forward(10)
        left(80)
        forward(9)
        right(70)
        forward(10)
        left(30)
        forward(2)
        right(220)
        forward(35)
        if abs(pos()) < 1:
            break
move_away()
reset()
'''
'''
#turtle spiral- looks like a sun sort of
penup()
for steps in range(100):
    stamp()
    forward(steps)
    right(30)
pendown()
move_away()
reset()
'''
'''
#turtle flower
penup()
for steps in range(100):
    stamp()
    forward(steps)
    right(50)
    left(100)
for steps in range(100,80,-1):
    stamp()
    forward(steps)
    right(50)
    left(100)
pendown()
move_away()
reset()
'''

#square spiral
shape('turtle')
penup()
for steps in range(200):
    left(180)
    stamp()
    left(180)
    forward(steps)
    right(50)
    left(100)

'''for steps in range(200,150,-1):
    stamp()
    forward(steps)
    right(50)
    left(100)
'''
pendown()
move_away()
reset()

'''
#sun 2.0?
while True:
        forward(10)
        left(220)
        forward(15)
        right(70)
        forward(20)
        left(80)
        forward(10)
        #stamp()
        right(70)
        forward(10)
        left(30)
        forward(20)
        right(220)
        forward(35)
        #stamp()
        if abs(pos()) < 1:
            break
move_away()
'''

