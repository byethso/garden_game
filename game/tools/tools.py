import pygame

class Tools(pygame.sprite.Sprite):
    def __init__(self, x, y, size, images, state):
        super().__init__()
        self.images = images
        self.state = state
        self.image = pygame.transform.scale(self.images[self.state], (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
