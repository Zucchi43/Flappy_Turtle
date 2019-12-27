import sys, pygame,os,random
from Turtle import *
from Background_Straws import *

pygame.init() #Start pygame modules
clock = pygame.time.Clock()
FPS = 60
size = width, height = 350,500 #Screen Size
speed = [2,2] #General Speed
black = 0,0,0 #The famous scolor: black
White = 255,255,255 #The famous color: White
gap = 125 #gap between straws
screen = pygame.display.set_mode(size)
Score = 0
Scored = False #Flag to check if turtle went through a straw
High_Score = 0 #Biggest score in that session of play
Playing = False #Flag to start the game
BackGround = Background('Images/Sea_background.png',[0,0])
Turtle = Turtle_class()
Ground_straw = Straw_class(0,height ,width,50,False)
Roof_straw = Straw_class(0,0,width,0,False)
Straws = []
Time_passed = 0

#Function to restart the straws and return a new Turtle
def Restart(Turtle):
    while(len(Straws)>0): Straws.pop()
    del Turtle
    return Turtle_class()

while 1:
    clock.tick(FPS)
    Time_passed += clock.get_time()
    screen.fill(White)
#HANDLER FOR EVENTS LIKE A KEY IS PRESSED
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                Playing = True
                Turtle.Fly()
            elif event.key == pygame.K_ESCAPE:
                quit()

            elif event.key == pygame.K_r:
                Turtle = Restart(Turtle)
                Playing = False
                Time_passed = 0
                Score = 0
        
        elif (event.type ==pygame.MOUSEBUTTONDOWN):
            if pygame.mouse.get_pressed()[0]:
                if Turtle.collided == False:
                    Playing = True
                    Turtle.Fly()
                elif Turtle.collided == True:
                    Turtle = Restart(Turtle)
                    Playing = False
                    Time_passed = 0
                    Score = 0


#DETECT COLLISION
    if Turtle.rect.colliderect(Ground_straw.rect) or Turtle.rect.colliderect(Roof_straw.rect):
        if Turtle.collided == False :Time_passed = 0
        Turtle.Collided()


    for straw in Straws:
        if Turtle.rect.colliderect(straw.rect) and Playing == True:
            if Turtle.collided == False :Time_passed = 0
            Turtle.Collided()

#Each X seconds create a pair of straws to try to kill the turtle with random heights
    if Time_passed > 1300 and Turtle.collided == False and Playing == True:
        Time_passed = 0
        Random_number = random.randrange(30,height-200,1)
        Straws.append(Straw_class(width,0,50,Random_number,True))
        Straws.append(Straw_class(width,Random_number+gap,50,height - Random_number + gap,False))


#If a Straw is out of bound delete the pair
    for straws in Straws:
        if(straws.rect.right < 0):
            Straws.pop(0)
            Straws.pop(0)
            Scored = False

#If the turtle collided reset the game after 3 sec
    #if Turtle.collided == True and Time_passed > 3000:
       # Turtle = Restart(Turtle) 
       # Playing = False
       # Time_passed = 0
        #Score = 0

#When the game starts or the player lost display the highscore and a message of how to play
    if pygame.font and Playing == False:
        font = pygame.font.Font(None, 46)
        text = font.render("HIGH_SCORE: " + str(High_Score), 1, black)
        textpos = text.get_rect(centerx=width/2,centery=height/3)
        font2 = pygame.font.Font(None, 46)
        text2 = font.render("SAVE THE TURTLE!!", 1, black)
        text2pos = text.get_rect(centerx=width/2 - 25,centery=height/2)

    if Turtle.collided == True:
        font2 = pygame.font.Font(None, 46)
        text2 = font.render("GAME OVER", 1, black)
        text2pos = text.get_rect(centerx=width/2-95,centery=height/2)

#UPDATE AND DISPLAY THE SCORE 
    if(len(Straws)>0):
        if(Turtle.rect.right > Straws[0].rect.right and Scored == False ):
            Score += 1
            if Score > High_Score: High_Score = Score
            Scored = True

    if pygame.font and Playing == True:
        font = pygame.font.Font(None, 46)
        text = font.render(str(Score), 1, black)
        textpos = text.get_rect(centerx=width/2,centery=25)


#UPDATE AND DISPLAY STUFF
    if Playing==True :Turtle.update()
    screen.blit(BackGround.image, BackGround.rect)
    for straws in Straws:
        if Turtle.collided == False and Playing == True: straws.update()
        screen.blit(straws.image, straws.rect)
    screen.blit(Turtle.image, Turtle.rect)
    screen.blit(Ground_straw.image, Ground_straw.rect)
    screen.blit(Roof_straw.image, Roof_straw.rect)
    screen.blit(text, textpos)
    if Turtle.collided or Playing is False : screen.blit(text2, text2pos)
    pygame.display.flip()


