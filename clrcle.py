import pygame 
pygame.init()
screen=pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
    pygame.draw.circle(screen,(255,255,255),(60,60),30)
    pygame.draw.circle(screen,(255,255,255),(120,120),30,4)
    pygame.display.flip()   