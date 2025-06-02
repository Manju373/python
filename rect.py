import pygame 
pygame.init()
screen=pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(60,60,40,40))
    pygame.display.flip()   