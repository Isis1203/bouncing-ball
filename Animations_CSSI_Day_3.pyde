ball_y = 100
y_speed = 4 #switching the speed of the ball 
ball_x = 100 #added new variables to make the ball go left and right
x_speed = 4

def setup():
    size(500, 500) 
    
def draw():
    global ball_y
    global ball_x
    background(200, 200, 200) #added the background in order for one ball to show at a time
    ellipse (ball_x, ball_y, 100, 100) 
    line(0, 0, 0, 0)
    line(500, 0, 500, 500) 
    line(0, 500, 500, 500) 
    line(500, 500, 500, 500) 
    
    if ball_y > 450:
        global y_speed #as before, I had to use global to call the variable down to this line of code
        print("BOUNCE") #bounce appeared at the bottom in the text box therefore, the barrier is on the right track 
        y_speed = -4 #made the ball reverse 
        #now add another "if" statement to get the ball bounce back and forth* 
    ball_y = ball_y + y_speed #made the ball faster, "if statement still needed to make the ball bounce" 

    if ball_y < 50:
        global y_speed 
        print("BOUNCE2") 
        y_speed = 4 
        
    if ball_x > 450:
        global x_speed
        print("BOUNCEL") 
        x_speed = -3
    ball_x = ball_x + x_speed 
    
    if ball_x < 50:
        global x_speed 
        print("BOUNCER")
        x_speed = 3 
    print(ball_x, x_speed)
        
    
    
    

    
