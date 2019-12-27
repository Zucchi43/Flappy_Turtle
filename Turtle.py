import pygame

size = width, height = 350,500 #Screen Size
gravity = 0.035 #gravity accel

class Turtle_class (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/Turtle_32.png')
        #self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.inflate(21,21)
        self.rect.move_ip((20,height/3))
        self.vel = [0, 0]
        self.accel = [0,0]
        self.collided = False
    
    def update(self):
        if self.collided == False:
            if self.accel[1] < 0.5 : self.accel[1] += gravity
            self.vel[0] += self.accel[0]
            self.vel[1] += self.accel[1]
            self.rect.move_ip(*self.vel)

    def Collided(self):
        #self.image.fill((255,0,0))
        self.rect.move((100,-50))
        self.accel[1] = 0
        self.vel[1] = 0
        self.collided = True
    
    def Fly(self):
        self.vel[1] = -6
        self.accel = [0,0]

    def death(self):
        if self.accel[1] < 0.5 : self.accel[1] += gravity
        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]
        self.rect.move_ip(*self.vel)

#Function to restart the straws and return a new Turtle
def Restart(Turtle):
    while(len(Straws)>0): Straws.pop()
    del Turtle
    return Turtle_class()