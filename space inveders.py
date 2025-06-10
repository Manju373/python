import math 
import pygame
import random
sw =800
sh = 400
psx = 370
psy = 230
esx = 2
esy = 20
collision =20
bull_speed = 10
got = psy-20

pygame.init()
screen = pygame.display.set_mode((sw,sh))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('background.png')
p_img=pygame.image.load('player.png')
e_img=pygame.image.load('enemy.png')
b_img=pygame.image.load('bullet.png')

font = pygame.font.Font("freetransbold.ttf",32)
Overfont=pygame.font.Font("freetransbold.ttf",64)
enemy =[
    {
        "x":random.randint(0, sw -64),
        "y":random.randint(50,150),
        "dx":esx
    }
    for _ in range(6)
]