from graphics import *
import random
import time
class Artwork:
    def __init__(self,is_foil, image):
        self.is_foil = is_foil
        self.correct = 0
        self.wrong = 0
        self.image = image
        self.seen = False

    def get_foil(self):
        return self.is_foil
    
    def get_correct(self):
        return self.correct
    
    def get_wrong(self):
        return self.wrong
    
    def get_image(self):
        return self.image
    
    def get_seen(self):
        return self.seen
    
    def was_seen(self):
        self.seen = True
    
    def increment_correct(self):
        self.correct +=1

    def increment_wrong(self):
        self.wrong +=1


def greeting(win):
    greeting = Text(Point(500,150), "Hello!")
    greeting.draw(win)
    message = Text(Point(500,250), "You will be asked if you remember seeing certain artworks.\n More instructions will be provided when relevant.\n\n\nIf you wish to continue hit the next button.")
    message.draw(win)
def clear_window(win, width, height):
    cover_screen = Rectangle(Point(0,0), Point(width,height))
    cover_screen.setFill("white")
    cover_screen.draw(win)
def button_creator(win,x1,y1,x2,y2,text):
    new_button = Rectangle(Point(x1,y1), Point(x2,y2))
    new_button.draw(win)
    new_button.setFill(color_rgb(130, 0, 100))
    center_point = new_button.getCenter()
    button_text = Text(center_point, text)
    button_text.draw(win)
def in_button_box(win, x1, y1, x2, y2, x, y):
    if(x >= x1 and x <=x2):
        if(y>=y1 and y<=y2):
            return True
    elif(x >= x2 and x <=x1):
        if(y>=y2 and y<=y1):
            return True
    else:
        return False
def add_input_box(win,x,y, width):
    inputBox = Entry(Point(x,y), width)
    inputBox.draw(win)
    return inputBox
def main():
    win = GraphWin("Memory", 1000, 600)
    greeting(win)
    next_x1 = 800
    next_y1 = 475
    next_x2 = 900
    next_y2 = 520
    button_creator(win,next_x1,next_y1,next_x2,next_y2,"Next")
    clickPoint = win.getMouse() # pause for click in window
    x = clickPoint.getX()
    y = clickPoint.getY()
    while(in_button_box(win,next_x1,next_y1,next_x2,next_y2,x,y)!= True):
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
    #create all images
    #add images to array
    #blank correct images array
    #blank incorrect images array
    #input box and next button
    #loop displaying image and getting feedback
        #choose random number, if not seen display
        #show image, instructions
        #get input from button when hit
        #add 1 to wrong or correct
        #add wrong into list of images -- the index of it
        #add correct into list of images -- the index of it
        #seen = true
    #once all images have been seen print correct array and wrong array
    #print("Take a picture of the results!")
    #add data into notebook for video




    


main()