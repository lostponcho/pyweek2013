import pygame
from pygame.locals import *

import animation
import random

# Collision rects should be floor rects - to work with the wall images
# Small rects for collisions
# Get data from resource list
# Use animation object for different frames
# (Separate class for animated sprites, so we only update them if needed)
# Need to display with offsets (i.e. camera)


class Player(object):
    """Because the player will change control of entities, this wrapper object is needed.
    It temporarily replaces the AI of the entity, putting it back when we lose control.
    """
    def __init__(self, world, entity):
        self.world = world
        self.entity = entity
        self.ai = None
        self.old_ai = self.entity.ai
        self.entity.ai = self.ai

class Entity(object):
    def __init__(self, world, pos, animation, collision, ai):
        self.ai = None
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
        self.dpos.x = random.randint(-10, 10) 
        self.dpos.y = random.randint(-10, 10) 

    def draw(self, surface, camera, tick):
        self.animation.draw(surface, (self.pos.x - camera.x, self.pos.y - camera.y), tick)
        
