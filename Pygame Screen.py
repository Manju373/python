import pygame
pygame.init()
b=pygame.display.set_mode((500,500))
a=pygame.image.load("game screen.jpg ").convert_alpha()
c=pygame.transform.scale(a,(300,300))
while True :
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
    b.fill((58,58,58))
    b.blit(c,(300,300))
    pygame.display.flip()
