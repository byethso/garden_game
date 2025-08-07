import pygame
import random

WIDTH = 800
HEIGHT = 650

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GLOVE=(121, 192, 240)


class Patch(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

class Seed(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))

class WateringCan(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

class Hoe(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))

class Glove(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        self.image.fill(GLOVE)
        self.rect = self.image.get_rect(topleft=(x, y))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

x=110
y=220
size=50
seed=Seed(x,y,size)
all_sprites.add(seed)

x=110
y=350
size=50
watering_can=WateringCan(x,y,size)
all_sprites.add(watering_can)

x=580
y=220
size=50
hoe=Hoe(x,y,size)
all_sprites.add(hoe)

x=580
y=350
size=50
glove=Glove(x,y,size)
all_sprites.add(glove)

plot_size = 100
plot_padding = 30
start_x = 190
start_y = 130

all_patches=[]
for row in range(3):
    for col in range(3):
        x = start_x + col * (plot_size + plot_padding)
        y = start_y + row * (plot_size + plot_padding)
        patch = Patch(x, y, plot_size)
        all_patches.append(patch)
        all_sprites.add(patch)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  #координаты клика

            for patch in all_patches: #находится ли точка клика внутри прямоугольника спрайта
                if patch.rect.collidepoint(mouse_pos):
                   patch.change_color()

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
