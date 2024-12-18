# https://youtu.be/3_S9lz5viOg

import turtle as tur
import time


class Fibonacci:
    def __init__(self, max_width):
        self.list = [0, 1]
        while self.list[len(self.list)-1] < max_width:
            self.i = self.list[len(self.list)-1] + self.list[len(self.list)-2]
            self.list.append(self.i)

    def main(self, x, y, square_colour, arc_colour):
        self.square(square_colour, x, y)
        self.arc(arc_colour, x, y)

    def square(self, colour, x, y):
        tur.pu()
        tur.goto(x, y)
        tur.seth(270)
        tur.color(colour)
        tur.pd()
        tur.width(3)
        tur.speed(5)
        for i in self.list:
            for j in range(5):
                tur.forward(i)
                tur.right(90)
            tur.forward(i)

    def arc(self, colour, x, y):
        tur.pu()
        tur.goto(x, y)
        tur.seth(90)
        tur.color(colour)
        tur.pd()
        tur.width(2)
        tur.speed(1)
        for i in self.list:
            tur.circle(-i, 90)


x = -232
y = -143
while True:
    tur.bgcolor("black")
    tur.ht()
    fibonacci = Fibonacci(500).main(x, y, "white", "white")
    time.sleep(10)
    tur.reset()