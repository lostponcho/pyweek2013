import resourcemanager

import random
import math

# Behaviours:

# - Behaviour trees don't really allow the mixing of behaviours

# Only update 1/n of the AIs each tick, and keep record of chosen behaviour + plan


# Suicide - charge largest group of enemies
# Heal - heal nearest damaged ally - play off damage vs. distance (when are allies not worth saving)
# Avoid explosions - don't charge next to an ally suicide
# Cast AoE
# ranged attack - aim for clear LoS
# charge/melee attack
# pathfind
# explore (I don't think we're going to do Fog of War, so this may be moot.)
# Stick near allies.
# Follow / guard
# Surround
# Don't cluster too close to allies.
# Flee - away from enemies, near allies (annoying for enemies?)
# Use ability (i.e. aid allies? ) - Actions need to be queriable
# log relative scores of behaviours, and chosen behaviour + entity ID + other events that happen to that entity
# chosen action vs. chosen behaviour

def distance(r1, r2):
    return math.sqrt((r1.x - r2.x) ** 2 + (r1.y - r2.y) ** 2)


def die_on_animation_end(entity):
    if entity.animation.is_done():
        entity.remove = True

def spider_ai(entity):
    entity.dpos.x = random.randint(-120, 120)
    entity.dpos.y = random.randint(-120, 120)
    
    if abs(entity.dpos.x) > abs(entity.dpos.y):
        if entity.dpos.x > 0:
            entity.animation.change(resourcemanager.animation_states["spider right"])
        else:
            entity.animation.change(resourcemanager.animation_states["spider left"])
    else:
        if entity.dpos.y > 0:
            entity.animation.change(resourcemanager.animation_states["spider down"])
        else:
            entity.animation.change(resourcemanager.animation_states["spider up"])
            
def imp_ai(entity):
    entity.dpos.x = random.randint(-120, 120)
    entity.dpos.y = random.randint(-120, 120)
    
    if abs(entity.dpos.x) > abs(entity.dpos.y):
        if entity.dpos.x > 0:
            entity.animation.change(resourcemanager.animation_states["imp right"])
        else:
            entity.animation.change(resourcemanager.animation_states["imp left"])
    else:
        if entity.dpos.y > 0:
            entity.animation.change(resourcemanager.animation_states["imp down"])
        else:
            entity.animation.change(resourcemanager.animation_states["imp up"])
            
def peasant_ai(entity):
    player_pos = entity.world.player.entity.pos

    player_dist = distance(player_pos, entity.pos)
    if player_dist < 200:
        xdir = player_pos.x - entity.pos.x
        ydir = player_pos.y - entity.pos.y

        entity.dpos.x = max(-entity.speed, min(entity.speed, xdir))
        entity.dpos.y = max(-entity.speed, min(entity.speed, ydir))
    else:
        entity.dpos.x = random.randint(-entity.speed, entity.speed)
        entity.dpos.y = random.randint(-entity.speed, entity.speed)        
    
    if abs(entity.dpos.x) > abs(entity.dpos.y):
        if entity.dpos.x > 0:
            entity.animation.change(resourcemanager.animation_states["peasant right"])
        else:
            entity.animation.change(resourcemanager.animation_states["peasant left"])
    else:
        if entity.dpos.y > 0:
            entity.animation.change(resourcemanager.animation_states["peasant down"])
        else:
            entity.animation.change(resourcemanager.animation_states["peasant up"])
            
def knight_ai(entity):
    player_pos = entity.world.player.entity.pos

    player_dist = distance(player_pos, entity.pos)
    if player_dist < 400:
        xdir = player_pos.x - entity.pos.x
        ydir = player_pos.y - entity.pos.y

        entity.dpos.x = max(-entity.speed, min(entity.speed, xdir))
        entity.dpos.y = max(-entity.speed, min(entity.speed, ydir))
    else:
        entity.dpos.x = random.randint(-entity.speed, entity.speed)
        entity.dpos.y = random.randint(-entity.speed, entity.speed)        
    
    if abs(entity.dpos.x) > abs(entity.dpos.y):
        if entity.dpos.x > 0:
            entity.animation.change(resourcemanager.animation_states["knight right"])
        else:
            entity.animation.change(resourcemanager.animation_states["knight left"])
    else:
        if entity.dpos.y > 0:
            entity.animation.change(resourcemanager.animation_states["knight down"])
        else:
            entity.animation.change(resourcemanager.animation_states["knight up"])
