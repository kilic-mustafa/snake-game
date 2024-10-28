import turtle,time,random,playsound,threading,pygame


theList =[]
scor = 0
maxScor = 0

pygame.mixer.init()
woosh_sound = pygame.mixer.Sound("woosh.mp3")
negative_sound = pygame.mixer.Sound("negative_action.mp3")
game_sound = pygame.mixer.Sound("game_music.mp3")
woosh_played = False
negative_played = False

game_sound.play(-1)

w = turtle.Screen()
w.title("Snake Game")
w.setup(600,600)
w.colormode(255)
w.bgcolor(0,40,0)
w.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("red")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

def moving():
    if snake.direction == "up": 
        y = snake.ycor() 
        snake.sety(y+20)
    if snake.direction == "down": 
        y = snake.ycor() 
        snake.sety(y-20)
    if snake.direction == "right": 
        x = snake.xcor() 
        snake.setx(x+20)
    if snake.direction == "left": 
        x = snake.xcor() 
        snake.setx(x-20)

def goUp():
    if snake.direction != "down":
        snake.direction = "up"
def goDown():
    if snake.direction != "up":
        snake.direction = "down"
def goRight():
    if snake.direction != "left":
        snake.direction = "right"
def goLeft():
    if snake.direction != "right":
        snake.direction = "left"

w.listen()
w.onkeypress(goUp,"Up")
w.onkeypress(goDown,"Down")
w.onkeypress(goLeft,"Left")
w.onkeypress(goRight,"Right")

forage = turtle.Turtle()
forage.speed(0)
forage.shape("circle")
forage.color("yellow")
forage.penup()
forage.goto(0,100)

def eat():
    global scor,maxScor,woosh_played
    if snake.distance(forage) < 20:
        woosh_sound.play()
        woosh_played = True
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        forage.goto(x,y)

        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("circle")
        tail.color("brown")
        tail.penup()
        theList.append(tail)
        
        scor += 5
        if scor > maxScor:
            maxScor = scor
        w.title("Scor: {}  |  The Highest Scor: {}".format(scor,maxScor))

    length = len(theList)
    for index in range(length-1,0,-1):
        x = theList[index-1].xcor()
        y = theList[index-1].ycor()
        theList[index].goto(x,y)

    if len(theList) > 0:
        x = snake.xcor()
        y = snake.ycor()
        theList[0].goto(x,y)
            
def starting():
    global scor
    time.sleep(0.1)
    snake.goto(0,0)
    snake.direction = "stop"
    for joint in theList:
        joint.goto(1000,1000)
    theList.clear()
    scor = 0
    w.title("Scor: {}  |  The Highest Scor: {}".format(scor,maxScor))

while True:
    w.update()
    eat()
    moving()
    
    if snake.xcor() > 280:
        snake.setx(-280)
        snake.direction = "right"
    elif snake.xcor() < -280:
        snake.setx(280)
        snake.direction = "left"
    elif snake.ycor() > 280:
        snake.sety(-280)
        snake.direction = "up"
    elif snake.ycor() < -280:
        snake.sety(280)
        snake.direction = "down" 
        
    for joint in theList:
        if joint.distance(snake) < 20:
             if not negative_played:
                 negative_sound.play()
                 negative_played = True 
             starting()
    time.sleep(0.1)
    
    woosh_played = False
    negative_played = False
    
w.mainloop()
        
