import pygame
from pygame.locals import *

import resourcemanager
import animation
import ai

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
    def __init__(self, world, pos, animation, collision, ai, name="Unnamed"):
        """All components should be optional.
        Track our entries in the world lists.
        """
        self.ai = ai
        self.animation = animation
        self.pos = pos.copy()
        self.dpos = pygame.Rect(0,0,0,0)
        self.remove = False
        self.name = name

    def move(self, dx, dy):
        self.rect.move(dx, dy)

    def animation_update(self):
        self.animation.update()
        
    def move_update(self):
        self.pos.x += self.dpos.x
        self.pos.y += self.dpos.y
        self.dpos.x = 0
        self.dpos.y = 0

    def ai_update(self):
        if self.ai:
            self.ai(self)

    def draw(self, surface, camera):
        self.animation.draw(surface, (self.pos.x - camera.x, self.pos.y - camera.y))

def make_small_explosion(world, pos):
    return Entity(world,
                  pos,
                  animation.Animation(resourcemanager.animation_states["small explosion"]),
                  pygame.Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Small Explosion")

def make_medium_explosion(world, pos):
    return Entity(world,
                  pos,
                  animation.Animation(resourcemanager.animation_states["medium explosion"]),
                  pygame.Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Medium Explosion")

def make_large_explosion(world, pos):
    return Entity(world,
                  pos,
                  animation.Animation(resourcemanager.animation_states["large explosion"]),
                  pygame.Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Large Explosion")
