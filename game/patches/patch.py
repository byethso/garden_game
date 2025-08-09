import pygame

from game.patches.patches_states import PatchesStates


class Patch(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.size = size
        self.state = PatchesStates.EMPTY
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.start_time = 0

    def change_state(self, state):
        self.state = state
        self.image = pygame.transform.scale(self.images[self.state], (self.size, self.size))
        if self.state == PatchesStates.HOED_WATERED_SEEDED:
            self.start_time = pygame.time.get_ticks()

    def update(self):
        super().update()
        now_time = pygame.time.get_ticks()
        if now_time - self.start_time >= 5000 and self.state == PatchesStates.HOED_WATERED_SEEDED:
            self.state = PatchesStates.GROWING
            self.image = pygame.transform.scale(self.images[self.state], (self.size, self.size))
        elif now_time - self.start_time >= 10000 and self.state == PatchesStates.GROWING:
            self.change_state(PatchesStates.HARVESTED)
