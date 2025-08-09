import pygame

from configurations.game_configurations import GameConfigurations
from tools.glove import Glove
from tools.hoe import Hoe
from patches.patch import Patch
from patches.patches_states import PatchesStates
from tools.seed import Seed
from tools.tool_type import ToolType
from tools.watering_can import WateringCan


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Garden Game")
        self.screen_width = 800
        self.screen_height = 650
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.all_sprites = pygame.sprite.Group()
        self.all_patches = pygame.sprite.Group()
        self.tools = pygame.sprite.Group()
        self.configuration = GameConfigurations()

        self.images = {
            PatchesStates.EMPTY: pygame.image.load("pics/empty.PNG"),
            ToolType.GLOVE: pygame.image.load("pics/glove.PNG"),
            PatchesStates.GROWING: pygame.image.load("pics/growing.PNG"),
            PatchesStates.HARVESTED: pygame.image.load("pics/harvested.PNG"),
            ToolType.HOE: pygame.image.load("pics/hoe.PNG"),
            PatchesStates.HOED: pygame.image.load("pics/hoed.PNG"),
            PatchesStates.HOED_SEEDED: pygame.image.load("pics/hoed_seeded.PNG"),
            PatchesStates.HOED_WATERED:pygame.image.load("pics/hoed_watered.PNG"),
            PatchesStates.HOED_WATERED_SEEDED: pygame.image.load("pics/hoed_watered_seeded.PNG"),
            ToolType.SEED: pygame.image.load("pics/seed.PNG"),
            ToolType.WATERING_CAN: pygame.image.load("pics/watering_can.PNG")
        }

        watering_can = WateringCan(self.configuration.watering_can.x, self.configuration.watering_can.y,
                                   self.configuration.watering_can.size, self.images)
        self.all_sprites.add(watering_can)
        self.tools.add(watering_can)

        glove = Glove(self.configuration.glove.x, self.configuration.glove.y, self.configuration.glove.size,
                      self.images)
        self.all_sprites.add(glove)
        self.tools.add(glove)

        hoe = Hoe(self.configuration.hoe.x, self.configuration.hoe.y, self.configuration.hoe.size,
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
                self.all_patches.add(patch)
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
                    elif self.all_patches.has(sprite):
                        if isinstance(self.selected_sprite, Hoe):
                            sprite.change_state(PatchesStates.HOED)
                        else:
                            self.selected_sprite = None

    def update(self):
        self.all_sprites.update(self)

    def draw(self):
        self.screen.fill((172, 214, 163))
        self.all_sprites.draw(self.screen)
        if self.selected_sprite is not None:
            pygame.draw.rect(self.screen, (111, 70, 54), self.selected_sprite.rect, 3)
        pygame.display.flip()
