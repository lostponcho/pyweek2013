import resourcemanager

import random


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
    entity.dpos.x = random.randint(-120, 120)
    entity.dpos.y = random.randint(-120, 120)
    
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
    entity.dpos.x = random.randint(-120, 120)
    entity.dpos.y = random.randint(-120, 120)
    
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
