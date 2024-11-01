from svg_turtle import SvgTurtle
import turtle

def draw_star(t):
   while True:
      t.forward(200)
      t.left(140)
      if abs(t.pos()) < 1:
         break
def curve(t): 
    for i in range(200): 
  
        # Defining step by step curve motion 
        t.right(1) 
        t.forward(1) 
def draw_flower(t):
   for repetitions in range(6):
      curve(t)
      t.left(140)
def draw_triangle(t):
   t.forward(50)
   t.right(120)
   t.forward(50)
   t.right(120)
   t.forward(50)
   t.right(120)
def draw_rectangle(t):
   t.forward(50)
   t.right(90)
   t.forward(110)
   t.right(90)
   t.forward(50)
   t.right(90)
   t.forward(110)
   t.right(90)
#save image
def write_file(draw_func, filename, width, height):
   t=SvgTurtle(width,height)
   
   draw_func(t)
   t.save_as(filename)

def main():
   write_file(draw_rectangle, 'demo.svg',800,800)


main()