import pygame
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Add Sprites")
wh=(255,255,255)
green=(0,255,0)
red=(255,0,0)
p= pygame.Rect(50,50,50,50)
o= pygame.Rect(300,200,60,60)
run = True
pv = True
speed =12
ov = True 
while run: 
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
    is1 = pygame.key.get_pressed()
    if is1[pygame.K_LEFT] :
        p.x -= speed
    if is1[pygame.K_RIGHT] :
        p.x += speed
    if is1[pygame.K_DOWN] :
        p.y += speed
    if is1[pygame.K_UP] :
        p.y -= speed
    if p.colliderect(o):
        ov =False
    screen.fill(wh)
    if pv :
        pygame.draw.rect(screen,green,p)
    if ov :
        pygame.draw.rect(screen,red,o)
    pygame.display.flip()