from graphics import *
import random
import time
def greeting(win):
    greeting = Text(Point(250,150), "Hello!")
    greeting.draw(win)
    message = Text(Point(250,250), "You will be asked how you feel when you look at certain artworks.\n You will answer on a scale of 1-5.\n More instructions will be provided when relevant.\n\n\nIf you wish to continue hit the next button.")
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
    #create window
    win = GraphWin("Classical Conditioning", 500, 500)
    #intro to experiment
    greeting(win)
    #c = Circle(Point(50,50), 10)
    #c.draw(win)
    #inputBox = Entry(Point(250,400), 5)
    #inputBox.draw(win)
    next_x1 = 200
    next_y1 = 375
    next_x2 = 300
    next_y2 = 420
    button_creator(win,next_x1,next_y1,next_x2,next_y2,"Next")
    clickPoint = win.getMouse() # pause for click in window
    x = clickPoint.getX()
    y = clickPoint.getY()
    while(in_button_box(win,next_x1,next_y1,next_x2,next_y2,x,y)!= True):
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
    #gather responses to images to find ones with positive feedback
    clear_window(win, 500, 500)
    #display instructions
    message = Text(Point(250,50), "Rate these artworks on a scale of 1-5.\n 1 is for the artwork makes you feel negative emotions\n3 is neutral\n 5 is the artwork makes you feel positive emotions\nWhen your done hit the submit button")
    message.draw(win)
    #input boxes
    input_box1 =add_input_box(win,100,250,3)
    input_box2 =add_input_box(win,250,250,3)
    input_box3 =add_input_box(win,400,250,3)
    input_box4 =add_input_box(win,100,450,3)
    input_box5 =add_input_box(win,250,450,3)
    input_box6 =add_input_box(win,400,450,3)
    #6 artworks to display
    Waterlillies = Image(Point(100,170),"Monet_small.gif")
    Waterlillies.draw(win)
    calf_bearer = Image(Point(250,170),"calf_bearer_small.gif")
    calf_bearer.draw(win)
    Signac = Image(Point(400,170),"Signac_small.gif")
    Signac.draw(win)
    varo = Image(Point(100,360),"varo_small.gif")
    varo.draw(win)
    van_gogh = Image(Point(250,360),"Van_Gogh_small.gif")
    van_gogh.draw(win)
    Krasner = Image(Point(400,360),"Krasner_small.gif")
    Krasner.draw(win)
    #images to show later
    Waterlillies_m = Image(Point(250,250),"monet_medium.gif")
    calf_bearer_m = Image(Point(250,250),"calf_bearer_medium.gif")
    Signac_m = Image(Point(250,250),"signac_medium.gif")
    varo_m = Image(Point(250,250),"varo_medium.gif")
    van_gogh_m = Image(Point(250,250),"van_gogh_medium.gif")
    Krasner_m = Image(Point(250,250),"Krasner_medium.gif")
    #minimalist images
    andre_m = Image(Point(250,250),"andre_medium.gif")
    judd_m = Image(Point(250,250),"judd_medium.gif")
    lewitt_m = Image(Point(250,250),"lewitt_medium.gif")
    morris_m = Image(Point(250,250),"morris_medium.gif")
    smith_m = Image(Point(250,250),"smith_medium.gif")
    stella_m = Image(Point(250,250),"stella_medium.gif")
    #array of minimalist images
    min_images = [andre_m,judd_m,lewitt_m,morris_m,smith_m,stella_m]
    #submit button
    x1 = 450
    y1 = 465
    x2 = 500
    y2 = 500
    button_creator(win,x1,y1,x2,y2,"Submit")
    clickPoint = win.getMouse() # pause for click in window
    x = clickPoint.getX()
    y = clickPoint.getY()
    while(in_button_box(win,x1,y1,x2,y2,x,y)!= True):
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
    #take input and store positive artworks in an array
    input1 = int(input_box1.getText())
    input2 = int(input_box2.getText())
    input3 = int(input_box3.getText())
    input4 = int(input_box4.getText())
    input5 = int(input_box5.getText())
    input6 = int(input_box6.getText())

    inputs = [input1,input2,input3,input4,input5,input6]
    initial_images = [Waterlillies_m,calf_bearer_m,Signac_m,varo_m, van_gogh_m,Krasner_m]
    positive_images = []
    for i in range(len(inputs)):
        if inputs[i] >3:
            positive_images.append(initial_images[i])
    print("num pos images",len(positive_images))
    win.close()
    iterations = 0
    test_average =0
    while(iterations <4 and test_average < 4):
        conditioning_random_num = random.randint(3,5)
        conditioning_average = 0
        test_average= 0
        c_iterations = 0
        #win = GraphWin("Classical Conditioning", 500, 500)
        ###########################################
        #conditioning
        ###########################################
        while(conditioning_average < 3 and c_iterations <4):
            c_total = 0
            conditioning_average = 0
            for x in range(conditioning_random_num):
                 win = GraphWin("Conditioning Trials", 500, 500)
                 message = Text(Point(250,50),"On a scale from 1-5 how does this artwork make you feel?")
                 message.draw(win)
                 #minimalist image
                 random_min = random.randint(0,5)
                 image = min_images[random_min]
                 image.draw(win)
                 #input box and submit button
                 c_input = add_input_box(win,250,480,3)
                 #submit button
                 x1 = 450
                 y1 = 465
                 x2 = 500
                 y2 = 500
                 button_creator(win,x1,y1,x2,y2,"Submit")
                 clickPoint = win.getMouse() # pause for click in window
                 x = clickPoint.getX()
                 y = clickPoint.getY()
                 while(in_button_box(win,x1,y1,x2,y2,x,y)!= True):
                     clickPoint = win.getMouse() # pause for click in window
                     x = clickPoint.getX()
                     y = clickPoint.getY()
                 #update total
                 c_response = int(c_input.getText())
                 c_total = c_total + c_response
                 #close window
                 win.close()
                 #positive images
                 random_positive = random.randint(0,(len(positive_images)-1))
                 #print("random",random_positive)
                 win = GraphWin("Classical Conditioning", 500, 500)
                 positive_image = positive_images[random_positive]
                 positive_image.draw(win)
                 time.sleep(2)
                 win.close()
            #update variables
            conditioning_average= c_total/conditioning_random_num
            print("conditioning average", conditioning_average)
        ##########################################
        #test conditioning
        ##########################################
            test_random_num = random.randint(2,3)
            test_average = 0
            t_total = 0
            for x in range(test_random_num):
                win = GraphWin("Critical Trials", 500, 500)
                message = Text(Point(250,50),"On a scale from 1-5 how does this artwork make you feel?")
                message.draw(win)
                #minimalist image
                random_min = random.randint(0,5)
                image = min_images[random_min]
                image.draw(win)
                #input box and submit button
                t_input = add_input_box(win,250,480,3)
                #submit button
                x1 = 450
                y1 = 465
                x2 = 500
                y2 = 500
                button_creator(win,x1,y1,x2,y2,"Submit")
                clickPoint = win.getMouse() # pause for click in window
                x = clickPoint.getX()
                y = clickPoint.getY()
                while(in_button_box(win,x1,y1,x2,y2,x,y)!= True):
                    clickPoint = win.getMouse() # pause for click in window
                    x = clickPoint.getX()
                    y = clickPoint.getY()
                #update total
                t_response = int(t_input.getText())
                t_total = t_total + t_response
                #close window
                win.close()
            test_average= t_total/test_random_num
            print("test average",test_average)
            c_iterations = c_iterations +1
        #conclude loop
        iterations= iterations +1
    #########################################
    #Extinction
    #################################
    e_random = random.randint(10,15)
    for x in range(e_random):
        win = GraphWin("Extinction", 500, 500)
        message = Text(Point(250,50),"On a scale from 1-5 how does this artwork make you feel?")
        message.draw(win)
        #minimalist image
        random_min = random.randint(0,5)
        image = min_images[random_min]
        image.draw(win)
        #input box and submit button
        t_input = add_input_box(win,250,480,3)
        #submit button
        x1 = 450
        y1 = 465
        x2 = 500
        y2 = 500
        button_creator(win,x1,y1,x2,y2,"Submit")
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
        while(in_button_box(win,x1,y1,x2,y2,x,y)!= True):
            clickPoint = win.getMouse() # pause for click in window
            x = clickPoint.getX()
            y = clickPoint.getY()
        #update total
        t_response = int(t_input.getText())
        t_total = t_total + t_response
        #close window
        win.close()

    win = GraphWin("Classical Conditioning", 500, 500)
    message = Text(Point(250,250), "Thank you for participating")
    message.draw(win)
    next_x1 = 200
    next_y1 = 375
    next_x2 = 300
    next_y2 = 420
    button_creator(win,next_x1,next_y1,next_x2,next_y2,"Close")
    clickPoint = win.getMouse() # pause for click in window
    x = clickPoint.getX()
    y = clickPoint.getY()
    while(in_button_box(win,next_x1,next_y1,next_x2,next_y2,x,y)!= True):
        clickPoint = win.getMouse() # pause for click in window
        x = clickPoint.getX()
        y = clickPoint.getY()
    win.close()
main()