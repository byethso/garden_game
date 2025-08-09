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

images = {
    "empty": pygame.image.load("empty.PNG"),
    "glove": pygame.image.load("glove.PNG"),
    "growing": pygame.image.load("growing.PNG"),
    "harvested": pygame.image.load("harvested.PNG"),
    "hoe": pygame.image.load("hoe.PNG"),
    "hoed": pygame.image.load("hoed.PNG"),
    "hoed_seeded": pygame.image.load("hoed_seeded.PNG"),
    "hoed_watered": pygame.image.load("hoed_watered.PNG"),
    "hoed_watered_seeded": pygame.image.load("hoed_watered_seeded.PNG"),
    "seed": pygame.image.load("seed.PNG"),
    "watering_can": pygame.image.load("watering_can.PNG")
}


class Patch(pygame.sprite.Sprite):
    def __init__(self,x,y,size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "empty"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

class Seed(pygame.sprite.Sprite):
    def __init__(self,x,y,size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "seed"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw_line(self, surface, color, width_line):
        pygame.draw.rect(surface, WHITE, self.rect, width_line)

class WateringCan(pygame.sprite.Sprite):
    def __init__(self,x,y,size,images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "watering_can"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

class Hoe(pygame.sprite.Sprite):
    def __init__(self,x,y,size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "hoe"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

class Glove(pygame.sprite.Sprite):
    def __init__(self,x,y,size,images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "glove"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tools=pygame.sprite.Group()
all_pathes=pygame.sprite.Group()

x=110
y=220
seed_size=70
seed=Seed(x,y,seed_size,images)
all_sprites.add(seed)
tools.add(seed)


x=110
y=350
watering_can_size=70
watering_can=WateringCan(x,y,watering_can_size,images)
all_sprites.add(watering_can)
tools.add(watering_can)


x=560
y=220
hoe_size=70
hoe=Hoe(x,y,hoe_size,images)
all_sprites.add(hoe)
tools.add(hoe)

x=560
y=350
glove_size=70
glove=Glove(x,y,glove_size,images)
all_sprites.add(glove)
tools.add(glove)

plot_size = 100
plot_padding = 30
start_x = 190
start_y = 130


for row in range(3):
    for col in range(3):
        x = start_x + col * (plot_size + plot_padding)
        y = start_y + row * (plot_size + plot_padding)
        patch = Patch(x, y, plot_size, images)
        all_sprites.add(patch)
        all_pathes.add(patch)


selected_sprite=None

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  #координаты клика
            for sprite in all_sprites:
                if sprite.rect.collidepoint(mouse_pos):
                    if tools.has(sprite):
                        if sprite==selected_sprite:
                            selected_sprite=None
                        else:
                            selected_sprite = sprite
                        break
                elif all_pathes.has(sprite):
                    selected_sprite=None


    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)

    if selected_sprite is not None:
        pygame.draw.rect(screen, WHITE, selected_sprite.rect, 3)
    pygame.display.flip()


pygame.quit()
