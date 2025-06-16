import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Two Sprites with Custom Color Change Event")
clock = pygame.time.Clock()

def random_color():
    return (random.randint(50,255), random.randint(50,255), random.randint(50,255))

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        self.color = random_color()
        self.image.fill(self.color)

sprite1 = ColorSprite(100, 170, random_color())
sprite2 = ColorSprite(400, 170, random_color())

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000)  

running = True
while running:
    screen.fill((255, 255, 255))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()