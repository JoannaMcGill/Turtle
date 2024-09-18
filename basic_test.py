from turtle import *

def reset():
    home()
    clearscreen()
#triangle
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#reset
reset()

#geometric pattern: spiral
'''for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

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

reset()
'''
'''
#star
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

reset()

#star but wider center: star 2
while True:
    forward(200)
    left(220)
    if abs(pos()) < 1:
        break
reset()
'''
for steps in range(9):
    left(200) 
    #star 2, range 4, left 90
    #star 2, range 9, left 200
    while True:
        forward(100)
        left(220)
        if abs(pos()) < 1:
            break
