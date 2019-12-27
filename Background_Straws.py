import pygame

size = width, height = 350,500 #Screen Size
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



class Straw_class (pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, size_x, size_y,inverted):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Images/canudo_mal_feito.png'), (size_x,size_y))
        if inverted: self.image = pygame.transform.rotozoom(self.image,180,1)
        self.rect = self.image.get_rect()
        self.rect.move_ip((start_x,start_y))
        self.vel = [0, 0]
        self.accel = [-4,0]

    def update(self):
        self.vel[0] = self.accel[0]
        self.vel[1] = self.accel[1]
        self.rect.move_ip(*self.vel)
