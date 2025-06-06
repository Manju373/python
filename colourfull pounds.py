import pygame,random
pygame.init()
clock = pygame.time.Clock()
blue = pygame.Color("Blue")
white = pygame.Color("White")
red = pygame.Color("Red")
yellow = pygame.Color("Yellow")
orange = pygame.Color("Orange")
black = pygame.Color("Black")
sprite1 = pygame.USEREVENT +1
bg = pygame.USEREVENT +2
bgcolour = pygame.Color("Green")
class Sprite(pygame.sprite.Sprite) :
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity =[random.choice([-1,1]),random.choice([-1,1])]
    def update(self) :
        self.rect.move_ip(self.velocity)
        boun=False
        if self.rect.left <=0 or self.rect.right >=500:
            boun = True
            self.velocity[0]=-self.velocity[0]
        if self.rect.top <=0 or self.rect.bottom >=500:
            boun = True
            self.velocity[1]=-self.velocity[1]
        if boun :
            pygame.event.post(pygame.event.Event(sprite1))
            pygame.event.post(pygame.event.Event(bg))

