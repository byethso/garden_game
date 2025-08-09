import pygame

class Patch(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "empty"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class Seed(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "seed"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class WateringCan(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "watering_can"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class Hoe(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "hoe"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class Glove(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.state = "glove"
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class GameConfigurations():
    def __init__(self):
        self.hoe = ObjectConfiguration(560, 220, 70,0)
        self.patch = ObjectConfiguration(190, 130, 100, 30)
        self.watering_can = ObjectConfiguration(110, 350, 70,0)
        self.glove = ObjectConfiguration(560, 350, 70,0)
        self.seed = ObjectConfiguration(110, 220, 70,0)

class ObjectConfiguration():
    def __init__(self,x,y,size,padding):
        self.x=x
        self.y=y
        self.size=size
        self.padding=padding


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Garden Game")
        self.screen_width = 800
        self.screen_height = 650
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.all_sprites = pygame.sprite.Group()
        self.all_pathes = pygame.sprite.Group()
        self.tools = pygame.sprite.Group()
        self.configuration=GameConfigurations()

        self.images = {
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

        watering_can = WateringCan(self.configuration.watering_can.x,self.configuration.watering_can.y,self.configuration.watering_can.size, self.images)
        self.all_sprites.add(watering_can)
        self.tools.add(watering_can)

        glove = Glove(self.configuration.glove.x,self.configuration.glove.y, self.configuration.glove.size,
                      self.images)
        self.all_sprites.add(glove)
        self.tools.add(glove)

        hoe = Hoe(self.configuration.hoe.x,self.configuration.hoe.y, self.configuration.hoe.size,
                  self.images)
        self.all_sprites.add(hoe)
        self.tools.add(hoe)

        seed = Seed(self.configuration.seed.x, self.configuration.seed.y, self.configuration.seed.size,
                    self.images)
        self.all_sprites.add(seed)
        self.tools.add(seed)

        for row in range(3):
            for col in range(3):
                x = self.configuration.patch.x + col * (
                            self.configuration.patch.size + self.configuration.patch.padding)
                y = self.configuration.patch.y + row * (
                            self.configuration.patch.size + self.configuration.patch.padding)
                patch = Patch(x, y, self.configuration.patch.size, self.images)
                self.all_sprites.add(patch)
                self.all_pathes.add(patch)
        self.selected_sprite = None
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_events(event)

            self.update()
            self.draw()
        pygame.quit()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # координаты клика
            for sprite in self.all_sprites:
                if sprite.rect.collidepoint(mouse_pos):
                    if self.tools.has(sprite):
                        if sprite == self.selected_sprite:
                            self.selected_sprite = None
                        else:
                            self.selected_sprite = sprite
                        break
                elif self.all_pathes.has(sprite):
                    self.selected_sprite = None

    def update(self):
        self.all_sprites.update(self)

    def draw(self):
        self.screen.fill((172, 214, 163))
        self.all_sprites.draw(self.screen)
        if self.selected_sprite is not None:
            pygame.draw.rect(self.screen, (111,70,54), self.selected_sprite.rect, 3)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
