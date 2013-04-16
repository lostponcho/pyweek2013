import pygame
from pygame.locals import *

# Collision rects should be floor rects - to work with the wall images
# Small rects for collisions
# Get data from resource list
# Use animation object for different frames
# (Separate class for animated sprites, so we only update them if needed)
# Need to display with offsets (i.e. camera)
class Entity(pygame.sprite.Sprite):
    def __init__(self, drawing, x, y):
        self.rect = pygame.Rect(x, y, self.drawing.w, self.drawing.h)
        self.img_rect = pygame.Rect(x, y, self.drawing.w, self.drawing.h)
        self.drawing = drawing

    def move(self, dx, dy):
        self.rect.move(dx, dy)
        self.img_rect(dx, dy)
