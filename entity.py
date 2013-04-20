import pygame
from pygame.locals import *

import resourcemanager
import animation
import ai

import math
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
    def __init__(self, world, pos, animation, collision, ai, name="Unnamed", speed=120):
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
        self.speed = speed
        self.hit_wall = False

    def animation_update(self):
        self.animation.update()

    def move(self, dx, dy):
        self.dpos.x += dx
        self.dpos.y += dy
        
    def move_update(self, tick):
        # int() is necessary as by default it gives us a negative bias
        dx, dy, self.hit_wall = self.world.map.collide(self.pos,
                                                       int(self.dpos.x * tick),
                                                       int(self.dpos.y * tick))

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
                  Rect(x, y, 36, 36),                  
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

def make_fireball(world, x, y, dx, dy, speed = 300):
    dist = math.sqrt(dx ** 2 + dy ** 2)
    dx *= speed / dist
    dy *= speed / dist    
    
    if 2 * abs(dy) > abs(dx):
        if dy > 0:
            anim = "fireball down"
        else:
            anim = "fireball up"
    elif 2 * abs(dx) > abs(dy):
        if dx > 0:
            anim = "fireball right"
        else:
            anim = "fireball left"
    elif dx > 0:
        if dy > 0:
            anim = "fireball down right"
        else:
            anim = "fireball up right"
    else:
        if dy > 0:
            anim = "fireball down left"
        else:
            anim = "fireball up left"
    
    return Entity(world,
                  Rect(x, y, 16, 16),                  
                  animation.Animation(resourcemanager.animation_states[anim]),
                  Rect(0, 0, 16, 16),
                  ai.make_fireball_ai(dx, dy),
                  "Fireball")

    
