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
        self.old_ai = self.entity.ai
        self.entity.ai = self
        self.dx, self.dy = 0, 0

    def __call__(self, entity):
        entity.move(self.dx, self.dy)
        

class Entity(object):
    def __init__(self, world, pos, animation, collision, ai, name="Unnamed"):
        """All components should be optional.
        Track our entries in the world lists.
        """
        self.world = world
        self.ai = ai
        self.animation = animation
        self.pos = pos.copy()
        self.dpos = Rect(0,0,0,0)
        self.remove = False
        self.name = name

    def animation_update(self):
        self.animation.update()

    def move(self, dx, dy):
        self.dpos.x += dx
        self.dpos.y += dy
        
    def move_update(self, tick):
        # int() is necessary as by default it gives us a negative bias
        dx, dy = self.world.map.collide(self.pos, int(self.dpos.x * tick), int(self.dpos.y * tick))

        self.pos.x += dx
        self.pos.y += dy
        self.dpos.x = 0
        self.dpos.y = 0

    def ai_update(self):
        if self.ai:
            self.ai(self)

    def draw(self, surface, camera):
        self.animation.draw(surface, (self.pos.x - camera.x, self.pos.y - camera.y))

def make_small_explosion(world, x, y):
    return Entity(world,
                  Rect(x, y, 64, 64),                                                      
                  animation.Animation(resourcemanager.animation_states["small explosion"]),
                  pygame.Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Small Explosion")

def make_medium_explosion(world, x, y):
    return Entity(world,
                  Rect(x, y, 64, 64),                                    
                  animation.Animation(resourcemanager.animation_states["medium explosion"]),
                  pygame.Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Medium Explosion")

def make_large_explosion(world, x, y):
    return Entity(world,
                  Rect(x, y, 64, 64),                  
                  animation.Animation(resourcemanager.animation_states["large explosion"]),
                  Rect(0, 0, 64, 64),
                  ai.die_on_animation_end,
                  "Large Explosion")

def make_spider(world, x, y):
    return Entity(world,
                  Rect(x, y, 31, 31), 
                  animation.Animation(resourcemanager.animation_states["spider down"]),
                  Rect(0, 0, 32, 32),
                  ai.spider_ai,
                  "Spider")

def make_lich(world, x, y):
    return Entity(world,
                  Rect(x, y, 31, 31),                  
                  animation.Animation(resourcemanager.animation_states["lich down"]),
                  Rect(0, 0, 32, 32),
                  None,
                  "Lich")
    
def make_peasant(world, x, y):
    return Entity(world,
                  Rect(x, y, 31, 31),                  
                  animation.Animation(resourcemanager.animation_states["peasant down"]),
                  Rect(0, 0, 32, 32),
                  ai.peasant_ai,
                  "Peasant")

    
def make_knight(world, x, y):
    return Entity(world,
                  Rect(x, y, 31, 31),                  
                  animation.Animation(resourcemanager.animation_states["knight down"]),
                  Rect(0, 0, 32, 32),
                  ai.knight_ai,
                  "Knight")

    
def make_imp(world, x, y):
    return Entity(world,
                  Rect(x, y, 31, 31),                  
                  animation.Animation(resourcemanager.animation_states["imp down"]),
                  Rect(0, 0, 32, 32),
                  ai.imp_ai,
                  "Imp")

    
