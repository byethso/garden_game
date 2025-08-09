import pygame

from patches_states import PatchesStates


class Patch(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.size = size
        self.state = PatchesStates.EMPTY
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_state(self, state):
        self.state = state
        self.image = pygame.transform.scale(self.images[self.state], (self.size, self.size))