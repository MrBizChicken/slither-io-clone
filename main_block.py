from constants import *
import pygame

class Main_block(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, color):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.color = color
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)


    def update(self):
        print("player made")
