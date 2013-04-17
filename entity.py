import pygame
from pygame.locals import *

import animation

# Collision rects should be floor rects - to work with the wall images
# Small rects for collisions
# Get data from resource list
# Use animation object for different frames
# (Separate class for animated sprites, so we only update them if needed)
# Need to display with offsets (i.e. camera)


class Entity(object):
    def __init__(self, world, pos, animation, collision):
        self.animation = animation
        self.rect = pygame.Rect(pos, (self.drawing.w, self.drawing.h))
        self.img_rect = pygame.Rect(x, y, self.drawing.w, self.drawing.h)
        self.drawing = drawing

    def move(self, dx, dy):
        self.rect.move(dx, dy)
        self.img_rect(dx, dy)

    def move_update(self):
        self.pos.x += self.dpos.x
        self.pos.y += self.dpos.y
        self.dpos.x = 0
        self.dpos.y = 0

    def ai_update(self):
        pass

    def draw(self, surface, camera, tick):
        self.animation.draw(surface, (self.pos.x - camera.x, self.pos.y - camera.y), tick)
        
