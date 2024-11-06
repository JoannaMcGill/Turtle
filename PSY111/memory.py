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
    hi = Text(Point(500,150), "Hello!")
    hi.draw(win)
    message = Text(Point(500,250), "You will be asked if you remember seeing certain artworks.\n More instructions will be provided when relevant.\n\n\nIf you wish to continue hit the next button.")
    message.draw(win)
    return hi,message
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
    hello,message =greeting(win)
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

    #image1 = Image(Point(250,250),"andre_medium.gif")
    #artwork1 = Artwork(False,image1)
    #Artwork.get_image(artwork1).draw(win)
    #Artwork.get_image(artwork1).undraw()
    
    #create all images
    avatar = Image(Point(250,250),"avatar.gif")
    books1 = Image(Point(250,250),"books1.gif")
    books2 = Image(Point(250,250),"books2.gif")
    books3 = Image(Point(250,250),"books3.gif")
    cc1 = Image(Point(250,250),"cc1.gif")
    cc2 = Image(Point(250,250),"cc2.gif")
    crystal = Image(Point(250,250),"crystal.gif")
    drseuss = Image(Point(250,250),"drseuss.gif")
    final_drawing = Image(Point(250,250),"final_drawing.gif")
    grandma = Image(Point(250,250),"grandma.gif")
    grandpa = Image(Point(250,250),"grandpa.gif")
    grinch = Image(Point(250,250),"grinch.gif")
    hallway = Image(Point(250,250),"hallway.gif")
    keys = Image(Point(250,250),"keys.gif")
    large_mandala =Image(Point(250,250),"large_mandala.gif")
    lb1 = Image(Point(250,250),"LaurelBurch1.gif")
    lb2 = Image(Point(250,250),"LaurelBurch2.gif")
    mary_poppins = Image(Point(250,250),"mary_poppins.gif")
    my_signac = Image(Point(250,250),"my_signac.gif")
    noplan = Image(Point(250,250),"noplan.gif")
    oil_color = Image(Point(250,250),"oil_color.gif")
    oil_final = Image(Point(250,250),"oil_final.gif")
    oil_flower = Image(Point(250,250),"oil_flower.gif")
    orchid = Image(Point(250,250),"orchid.gif")
    rose = Image(Point(250,250),"rose.gif")
    snoopy = Image(Point(250,250),"snoopy.gif")
    troll = Image(Point(250,250),"troll.gif")
    trumpet_flower = Image(Point(250,250),"trumpet_flower.gif")
    turtle = Image(Point(250,250),"turtle.gif")
    waterfall = Image(Point(250,250),"waterfall.gif")
    #create artwork objects
    foil1 = Artwork(False,avatar)
    foil2 = Artwork(False,books1)
    foil3 = Artwork(False,books2)
    foil4 = Artwork(False,books3)
    foil5 = Artwork(False,crystal)
    foil6 = Artwork(False,grandma)
    foil7 = Artwork(False,grandpa)
    foil8 = Artwork(False,grinch)
    foil9 = Artwork(False,rose)
    foil10 = Artwork(False,snoopy)
    foil11 = Artwork(False,troll)
    foil12 = Artwork(False,noplan)
    foil13 = Artwork(False,trumpet_flower)
    foil14 = Artwork(False,turtle)
    foil15 = Artwork(False,waterfall)
    art1 = Artwork(True,cc1)
    art2 = Artwork(True,cc2)
    art3 = Artwork(True,drseuss)
    art4 = Artwork(True,final_drawing)
    art5 = Artwork(True,hallway)
    art6 = Artwork(True,keys)
    art7 = Artwork(True,lb1)
    art8 = Artwork(True,lb2)
    art9 = Artwork(True,large_mandala)
    art10 = Artwork(True,mary_poppins)
    art11 = Artwork(True,my_signac)
    art12 = Artwork(True,oil_color)
    art13 = Artwork(True,oil_final)
    art14 = Artwork(True,oil_flower)
    art15 = Artwork(True,orchid)
    #add images to array
    all_images = [foil1,foil2,foil3,foil4,foil5,foil6,foil7,foil8,foil9,foil10,foil11,foil12,foil13,foil14,foil15,art1,art2,art3,art4,art5,art6,art7,art8,art9,art10,art11,art12,art13,art14,art15]
    #blank correct images array
    correct =[]
    #blank incorrect images array
    incorrect = []
    #remove text
    hello.undraw()
    message.undraw()
    #add instructions
    message = Text(Point(700,150), "Do you remember this artwork being displayed currently\n1 Definitely not\n2 Probably not\n3 Maybe\n4 Probably yes\n5 Definitely Yes")
    message.draw(win)
    #set up variables for loop
    num_seen = 0
    while(num_seen<len(all_images)):
    #input box and next button
        u_response = add_input_box(win,700,300,5)
        button_creator(win,next_x1,next_y1,next_x2,next_y2,"Submit")
        #loop displaying image and getting feedback
        #choose random number, if not seen display
        random_num =random.randint(0,len(all_images)-1)
        while(all_images[random_num].get_seen()):
            random_num =random.randint(0,len(all_images)-1)
        #show image, instructions
        all_images[random_num].get_image().draw(win)
        #get input from button when hit
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
        while(in_button_box(win,next_x1,next_y1,next_x2,next_y2,x,y)!= True):
            clickPoint = win.getMouse() # pause for click in window
            x = clickPoint.getX()
            y = clickPoint.getY()
        response = int(u_response.getText())
        foil = all_images[random_num].get_foil()
        #add 1 to wrong or correct
        if(foil == True):
            if response > 3:
                correct.append(random_num)
            else:
                incorrect.append(random_num)
        if(foil == False):
            if response > 3:
                incorrect.append(random_num)
            else:
                correct.append(random_num)
        all_images[random_num].was_seen()
        num_seen = num_seen +1
        all_images[random_num].get_image().undraw()
        #seen = true
    #once all images have been seen print correct array and wrong array
    print("correct: ",correct)
    print("incorrect: ", incorrect)
    #print("Take a picture of the results!")
    #add data into notebook for video




    


main()