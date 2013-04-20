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

def random_movement(entity):
    entity.dpos.x = random.randint(-8, 8) 
    entity.dpos.y = random.randint(-8, 8)

    # TODO: replace this with some state thing? Animation tree?
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
            
def random_movement(entity):
    entity.dpos.x = random.randint(-8, 8) 
    entity.dpos.y = random.randint(-8, 8)

    # TODO: replace this with some state thing? Animation tree?
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
        
class Sequence(object):
    """Stores a sequence of actions + tests that consitute a behaviour.
    """
    def __init__(self):
        pass

class AI(object):
    """Stores the state for the AI of an entity.
    """
    def __init__(self):
        pass
