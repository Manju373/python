import pygame
pygame.init()
a=pygame.display.set_mode((600,600))
b=pygame.image.load("coconut.jpg").convert_alpha()
c=pygame.transform.scale(b,(200,200))
while not False :
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    a.blit(c,(200,200))
    pygame.display.flip()