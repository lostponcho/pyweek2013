import pygame
from pygame.locals import *

class Image(object):
    """Very simple image object. Defines the source pygame image + the area of that image to draw.
    """
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect
    def draw(self, surface, pos):
        surface.blit(self.image, pos, self.rect)
