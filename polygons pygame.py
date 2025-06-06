import pygame 
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My first game screen")
white=(255,255,255)
black=(0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.fill(white)
            screen.blit((220,220))
            pygame.quit()
            pygame.display.flip()

