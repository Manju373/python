import pygame 
pygame.init()
screen= pygame.display.set_mode((400,400))
pygame.display.set_caption("New Window")
s=False
while not s:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()