import pygame

from game.configurations.game_configurations import GameConfigurations
from game.patches.patch import Patch
from game.patches.patches_states import PatchesStates
from game.tools.glove import Glove
from game.tools.hoe import Hoe
from game.tools.seed import Seed
from game.tools.tool_type import ToolType
from game.tools.watering_can import WateringCan


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
            PatchesStates.EMPTY: pygame.image.load("game/pics/empty.PNG"),
            ToolType.GLOVE: pygame.image.load("game/pics/glove.PNG"),
            PatchesStates.GROWING: pygame.image.load("game/pics/growing.PNG"),
            PatchesStates.HARVESTED: pygame.image.load("game/pics/harvested.PNG"),
            ToolType.HOE: pygame.image.load("game/pics/hoe.PNG"),
            PatchesStates.HOED: pygame.image.load("game/pics/hoed.PNG"),
            PatchesStates.HOED_SEEDED: pygame.image.load("game/pics/hoed_seeded.PNG"),
            PatchesStates.HOED_WATERED:pygame.image.load("game/pics/hoed_watered.PNG"),
            PatchesStates.HOED_WATERED_SEEDED: pygame.image.load("game/pics/hoed_watered_seeded.PNG"),
            ToolType.SEED: pygame.image.load("game/pics/seed.PNG"),
            ToolType.WATERING_CAN: pygame.image.load("game/pics/watering_can.PNG")
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
                    if self.tools.has(sprite): #обработка инструментов
                        if sprite == self.selected_sprite:
                            self.selected_sprite = None
                        else:
                            self.selected_sprite = sprite
                        break                             #старт обработки клетки
                    elif self.all_patches.has(sprite):    #пропалываем только если грядка пустая
                        if isinstance(self.selected_sprite, Hoe) and sprite.state == PatchesStates.EMPTY:
                            sprite.change_state(PatchesStates.HOED)
                        elif isinstance(self.selected_sprite, WateringCan):
                            if sprite.state == PatchesStates.HOED:
                                sprite.change_state(PatchesStates.HOED_WATERED)
                            elif sprite.state == PatchesStates.HOED_SEEDED:
                                sprite.change_state(PatchesStates.HOED_WATERED_SEEDED)
                            else: #если грядка не прополота или что-то другое, то ничего не происходит
                                continue
                        elif isinstance(self.selected_sprite, Seed):
                            if sprite.state == PatchesStates.HOED:
                                sprite.change_state(PatchesStates.HOED_SEEDED)
                            elif sprite.state == PatchesStates.HOED_WATERED:
                                sprite.change_state(PatchesStates.HOED_WATERED_SEEDED)
                        elif isinstance(self.selected_sprite, Glove) and sprite.state == PatchesStates.HARVESTED:
                            sprite.change_state(PatchesStates.EMPTY)
                        else:
                            self.selected_sprite = None

    def update(self): #убрала self из скобок
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((172, 214, 163))
        self.all_sprites.draw(self.screen)
        if self.selected_sprite is not None:
            pygame.draw.rect(self.screen, (111, 70, 54), self.selected_sprite.rect, 3)
        pygame.display.flip()
